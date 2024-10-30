class Candidate:
    def __init__(self, name=None, hmdb_identification=None, detection_status=None, smiles_id=None, clas=None,
                 formula=None):
        self.COMMON_NAME = name
        self.HMDB_ID = hmdb_identification
        self.STATUS = detection_status
        self.SMILES = smiles_id
        self.CLASS = clas
        self.CHEMICAL_FORMULA = formula

LOCATORS = {
    'mass': ['By.ID', 'query_masses'],
    'ion_mode': ['By.XPATH', '//*[@id="ms_search_ion_mode"]/option[1]'], 
    'adduct_type': ['By.XPATH', '//*[@id="adduct_type"]/option[2]'],
    'tolerance': ['By.ID', 'tolerance'],
    'search_button': ['By.NAME', 'commit'],
    'entry_table': ['By.CLASS_NAME', 'ms-search-table'],
    'alternate_search_button': ['By.CSS_SELECTOR', 'a.btn.btn-primary[aria-controls=".specdb-search-form"]'],
    'max_page_entries': ['By.XPATH', '//*[@id="DataTables_Table_0_length"]/label/select/option[4]'],
    'entry_link': ['By.XPATH', '//*[@id="DataTables_Table_0"]/tbody/tr[{}]/td[1]/a'],
    'entry_info_page_confirmation': ['By.XPATH', '//*[@id="identification"]/th'],
    'status': ['By.XPATH', "/html/body/main/table/tbody[1]/tr[3]/td"],
    'hmdb_id': ['By.XPATH', "/html/body/main/table/tbody[1]/tr[6]/td"],
    'compound_name': ['By.XPATH', "/html/body/main/table/tbody[1]/tr[9]/td"],
    'description': ['By.XPATH', "/html/body/main/table/tbody[1]/tr[10]/td"],
    'chemical_formula': ['By.XPATH', "/html/body/main/table/tbody[1]/tr[13]/td"],
    'smiles': ['By.XPATH', "/html/body/main/table/tbody[1]/tr[19]/td"],
    'chemical_class': ['By.XPATH', "/html/body/main/table/tbody[1]/tr[26]/td"]
}


SEARCH_PARAMS = {
    'mz_value': 292 ,
    'initial_tolerance': 0.03,
    'upper_bound': 3,
    'lower_bound': 1,
    'URL': 'https://hmdb.ca/spectra/ms/search'
}


