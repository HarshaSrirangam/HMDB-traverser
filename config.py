
elements = { # null -> element does not have options; value of 'null' key is the element's HTML locator
    'm/z': {
        'find_by': 'By.ID',
        'null': 'query_masses'
    },
    'ion_mode': {
        'find_by': 'By.XPATH',
        'positive': '//*[@id="ms_search_ion_mode"]/option[1]',
        'negative': '//*[@id="ms_search_ion_mode"]/option[2]',
        'neutral': '//*[@id="ms_search_ion_mode"]/option[3]'
    },
    'adduct_type': {
        'find_by': 'By.XPATH',
        'unknown': '//*[@id="adduct_type"]/option[1]',
        'M+H': '//*[@id="adduct_type"]/option[2]',
        'M+H-2H2O': '//*[@id="adduct_type"]/option[3]',
        'M+H-H2O': '//*[@id="adduct_type"]/option[4]',
        'M+NH4-H2O': '//*[@id="adduct_type"]/option[5]',
        'M+Li': '//*[@id="adduct_type"]/option[6]',
        'M+NH4': '//*[@id="adduct_type"]/option[7]',
        'M+Na': '//*[@id="adduct_type"]/option[8]',
        'M+CH3OH+H': '//*[@id="adduct_type"]/option[9]',
        'M+K': '//*[@id="adduct_type"]/option[10]',
        'M+ACN+H': '//*[@id="adduct_type"]/option[11]',
        'M+2Na-H': '//*[@id="adduct_type"]/option[12]',
        'M+DMSO+H': '//*[@id="adduct_type"]/option[13]',
        'M+2ACN+H': '//*[@id="adduct_type"]/option[14]',
        'M+IsoProp+Na+H': '//*[@id="adduct_type"]/option[15]',
        'M+H+HCOONa': '//*[@id="adduct_type"]/option[16]',
        '2M+H': '//*[@id="adduct_type"]/option[17]',
        '2M+NH4': '//*[@id="adduct_type"]/option[18]',
        '2M+Na': '//*[@id="adduct_type"]/option[19]',
        '2M+2H+3H2O': '//*[@id="adduct_type"]/option[20]',
        '2M+ACN+H': '//*[@id="adduct_type"]/option[21]',
        '2M+ACN+Na': '//*[@id="adduct_type"]/option[22]',
        '2M+H-H2O': '//*[@id="adduct_type"]/option[23]',
        'M+2H': '//*[@id="adduct_type"]/option[24]',
        'M+H+NH4': '//*[@id="adduct_type"]/option[25]',
        'M+H+Na': '//*[@id="adduct_type"]/option[26]',
        'M+H+K': '//*[@id="adduct_type"]/option[26]',
        'M+ACN+2H': '//*[@id="adduct_type"]/option[27]',
        'M+2Na': '//*[@id="adduct_type"]/option[28]',
        'M+2ACN+2H': '//*[@id="adduct_type"]/option[29]',
        'M+3ACN+2H': '//*[@id="adduct_type"]/option[30]',
        'M+3H': '//*[@id="adduct_type"]/option[31]',
        'M+2H+Na': '//*[@id="adduct_type"]/option[32]',
        'M+H+2Na': '//*[@id="adduct_type"]/option[33]',
        'M+3Na': '//*[@id="adduct_type"]/option[34]',
        'M+H+2K': '//*[@id="adduct_type"]/option[35]'
    },
    'tolerance': {
        'find_by': 'By.ID',
        'null': 'tolerance'
    },
    'search_button': {
        'find_by': 'By.NAME',
        'null': 'commit'
    },
    'entry_table': {
        'find_by': 'By.CLASS_NAME',
        'null': 'ms-search-table'
    },
    'alternate_search_button': {
        'find_by': 'By.CSS_SELECTOR',
        'null': 'a.btn.btn-primary[aria-controls=".specdb-search-form"]'
    },
    'max_page_entries': {
        'find_by': 'By.XPATH',
        'null': '//*[@id="DataTables_Table_0_length"]/label/select/option[4]' # has options, but always select option 4
    },
    'entry_link': {
        'find_by': 'By.XPATH',
        'null': '//*[@id="DataTables_Table_0"]/tbody/tr[{}]/td[1]/a' # has options, but seperate function will traverse compounds
    },
    'entry_info_page_confirmation': { # ensures page has loaded before extracting compound info
        'find_by': 'By.XPATH',
        'null': '//*[@id="identification"]/th'
    },
    'compound_info': { # compound information for extraction
        'find_by': 'By.XPATH',
        'status': "/html/body/main/table/tbody[1]/tr[3]/td",
        'hmdb_id': "/html/body/main/table/tbody[1]/tr[6]/td",
        'compound_name': "/html/body/main/table/tbody[1]/tr[9]/td",
        'description': "/html/body/main/table/tbody[1]/tr[10]/td",
        'chemical_formula': "/html/body/main/table/tbody[1]/tr[13]/td",
        'smiles': "/html/body/main/table/tbody[1]/tr[19]/td",
        'chemical_class': "/html/body/main/table/tbody[1]/tr[26]/td"
        }
    }

 # ADD OTHER 3 PARAMATERS AND ALL ADDUCT TYPES


SEARCH_PARAMS = {
    'user_m/z': 292.0708,
    'user_ion_mode': 'positive',
    'user_adduct_type': 'M+H',
    'user_initial_tolerance': 0.05,
    'upper_bound': 3,
    'lower_bound': 1,
    'URL': 'https://hmdb.ca/spectra/ms/search'
}


