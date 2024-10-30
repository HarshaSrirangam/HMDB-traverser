from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HMDB_config import Candidate, LOCATORS, SEARCH_PARAMS as SP
import time


def locate(driver, element):
    method, path = element
    if isinstance(method, str) and method.startswith('By.'):
        method = getattr(By, method.split('.')[1])
    elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((method, path))
    )
    return elem


def select(driver, element):
    locate(driver, element).click()


def enter_text(driver, element, keys=None):
    locate(driver, element).send_keys(keys)


def get_number_of_entries(driver):
    try:
        alert = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'alert-warning'))
        )
        return 0
    except:
        try:
            entries = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'dataTables_info'))
            ).text
            entries = entries.split()
            return int(entries[5])
        except Exception as e:
            print(f"Error getting entries: {e}")
            return


def initial_search(driver=None, mass=0, tolerance=0.05):
    enter_text(driver, LOCATORS['mass'], str(mass))
    select(driver, LOCATORS['ion_mode'])
    select(driver, LOCATORS['adduct_type'])
    enter_text(driver, LOCATORS['tolerance'], str(tolerance))
    select(driver, LOCATORS['search_button'])
    return get_number_of_entries(driver)


def tolerance_search(driver, tolerance):
    select(driver, LOCATORS['alternate_search_button'])
    tolerance_input = locate(driver, LOCATORS['tolerance'])
    tolerance_input.clear()
    enter_text(driver, LOCATORS['tolerance'], tolerance)
    select(driver, LOCATORS['search_button'])


def dynamic_search(driver, tolerance, upper_bound=5, lower_bound=1):
    temp_tolerance = tolerance
    best_tolerance = temp_tolerance
    best_entries = 100
    iteration = 1
    for _ in range(10):
        tolerance_search(driver, temp_tolerance)
        ent = get_number_of_entries(driver)

        if lower_bound <= ent <= upper_bound:
            break
        if ent < best_entries and ent != 0:
            best_entries = ent
            best_tolerance = temp_tolerance
        if ent > upper_bound:
            temp_tolerance = pow(temp_tolerance, 10 / 9)
            temp_tolerance = round(temp_tolerance, 4)
        elif ent < lower_bound:
            temp_tolerance = pow(temp_tolerance, 10 / 11)
            temp_tolerance = round(temp_tolerance, 4)
        iteration += 1
        if iteration > 10:
            tolerance_search(driver, best_tolerance)


def traverse_candidates(current_driver, final_entries):
    candidates = []
    for i in range(final_entries):
        entry_xpath = LOCATORS['entry_link'][1].format(i + 1)
        entry_locator = (By.XPATH, entry_xpath)
        select(current_driver, entry_locator)
        locate(current_driver, LOCATORS['entry_info_page_confirmation'])
        
        status = locate(current_driver, LOCATORS['status']).text
        hmdb_id = locate(current_driver, LOCATORS['hmdb_id']).text
        compound_name = locate(current_driver, LOCATORS['compound_name']).text
        chemical_formula = locate(current_driver, LOCATORS['chemical_formula']).text
        smiles = locate(current_driver, LOCATORS['smiles']).text
        chemical_class = locate(current_driver, LOCATORS['chemical_class']).text

        candidate = Candidate(compound_name, hmdb_id, status, smiles, chemical_class, chemical_formula)
        candidates.append(candidate)
        current_driver.back()
        time.sleep(1)
    return candidates


def results(initial_candidates, statuses):
    final_compounds = []
    for status in statuses:
        final_compounds.extend([cand for cand in initial_candidates if cand.STATUS.lower() == status])
        if final_compounds:
            break

    if final_compounds and final_compounds[0].STATUS != 'detected and quantified':
        print(f'\nThe following compound(s) are {final_compounds[0].STATUS.lower()}')
    for i, current_candidate in enumerate(final_compounds):
        print(f'\n'
              f'Compound {i + 1}:\n'
              f'Name: {current_candidate.COMMON_NAME}\n'
              f'Class: {current_candidate.CLASS}\n'
              f'HMDB ID: {current_candidate.HMDB_ID}\n'
              f'SMILES: {current_candidate.SMILES}\n'
              f'Chemical formula: {current_candidate.CHEMICAL_FORMULA}\n')


desired_statuses = [
    'detected and quantified',
    'detected but not quantified',
    'expected but not quantified',
    'predicted'
]

if __name__ == '__main__':
    try:
        service = Service(ChromeDriverManager().install())
        current_driver = webdriver.Chrome(service=service)
        current_driver.get(SP['URL'])

        entries = initial_search(current_driver, SP['mz_value'], SP['initial_tolerance'])
        if entries > SP['upper_bound'] or entries < SP['lower_bound']:
            dynamic_search(current_driver, SP['initial_tolerance'], SP['upper_bound'], SP['lower_bound'])

        final_entries = get_number_of_entries(current_driver)
        if final_entries > 0:
            select(current_driver, LOCATORS['max_page_entries'])
            initial_candidates = traverse_candidates(current_driver, final_entries)
            results(initial_candidates, desired_statuses)
        else:
            print("No entries found.")
    except Exception:
        print(f'Search failed. Ensure stable connection and try again.')
    finally:
        current_driver.quit()
