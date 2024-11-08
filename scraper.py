from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import elements, SEARCH_PARAMS as SP
from utils import Candidate


def locate_element(driver, element, method): # option argument should be 'null' if directly accessing the element without options
    if isinstance(method, str) and method.startswith('By.'):
        by_method = getattr(By, method.split('.')[1])
    else:
        raise ValueError
    return WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((by_method, element))
    )

    
def select(driver, element, method):
    locate_element(driver, element, method).click()


def enter_text(driver, element, method, text):
    locate_element(driver, element, method).send_keys(text)


def primary_search(driver):
    enter_text(driver, elements['m/z']['null'], elements['m/z']['find_by'], SP['user_m/z'])
    select(driver, elements['ion_mode'][SP['user_ion_mode']], elements['ion_mode']['find_by'])
    select(driver, elements['adduct_type'][SP['user_adduct_type']], elements['adduct_type']['find_by'])
    select(driver, elements['ccs_prediction_method'][SP['user_ccs_prediction_method']], elements['ccs_prediction_method']['find_by'])
    select(driver, elements['collision_cross_section_tolerance'][SP['user_collision_cross_section_tolerance']], elements['collision_cross_section_tolerance']['find_by'])
    enter_text(driver, elements['tolerance']['null'], elements['tolerance']['find_by'], SP['user_initial_tolerance'])
    select(driver, elements['search_button']['null'], elements['search_button']['find_by'])
    return get_number_of_entries(driver)
    

def get_number_of_entries(driver):
    try:

        alert = WebDriverWait(driver, 20).until(
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
        except Exception:
            return


def tolerance_search(driver, dummy_tolerance):
    select(driver, elements['alternate_search_button']['null'], elements['alternate_search_button']['find_by'])
    locate_element(driver, elements['tolerance']['null'], elements['tolerance']['find_by']).clear()
    enter_text(driver, elements['tolerance']['null'], elements['tolerance']['find_by'], dummy_tolerance)
    select(driver, elements['search_button']['null'], elements['search_button']['find_by'])


def dynamic_search(driver, incoming_entries):
    upper_bound = SP['upper_bound']
    lower_bound = SP['lower_bound']
    if lower_bound <= incoming_entries <= upper_bound:
        return
    temp_tolerance = SP['user_initial_tolerance']
    best_tolerance = temp_tolerance
    best_entries = 100
    iteration = 1
    for _ in range(10):
        tolerance_search(driver, temp_tolerance)
        entries = get_number_of_entries(driver)

        if lower_bound <= entries <= upper_bound:
            break
        if entries < best_entries and entries != 0:
            best_entries = entries
            best_tolerance = temp_tolerance
        if entries > upper_bound:
            temp_tolerance = pow(temp_tolerance, 10 / 9)
            temp_tolerance = round(temp_tolerance, 4)
        elif entries < lower_bound:
            temp_tolerance = pow(temp_tolerance, 10 / 11)
            temp_tolerance = round(temp_tolerance, 4)
        iteration += 1
        if iteration > 10:
            tolerance_search(driver, best_tolerance)


def traverse_candidates(driver):
    final_entries = get_number_of_entries(driver)
    common_locate_method = elements['compound_info']['find_by']
    candidates = []
    for i in range(final_entries):
        current_compound = elements['entry_link']['null'].format(i + 1)
        select(driver, current_compound, elements['entry_link']['find_by'])
        locate_element(driver, elements['entry_info_page_confirmation']['null'], elements['entry_info_page_confirmation']['find_by'])
        
        status = locate_element(driver, elements['compound_info']['status'], common_locate_method).text
        hmdb_id = locate_element(driver, elements['compound_info']['hmdb_id'], common_locate_method).text
        compound_name = locate_element(driver, elements['compound_info']['compound_name'], common_locate_method).text
        chemical_formula = locate_element(driver, elements['compound_info']['chemical_formula'], common_locate_method).text
        smiles = locate_element(driver, elements['compound_info']['smiles'], common_locate_method).text
        chemical_class = locate_element(driver, elements['compound_info']['chemical_class'], common_locate_method).text

        candidate = Candidate(compound_name, hmdb_id, status, smiles, chemical_class, chemical_formula)
        candidates.append(candidate)
        driver.back()
    return candidates
