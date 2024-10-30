HMDB-Traverser Version 1: A tool for matching mass spectrometry data to metabolites via the Human Metabolome Database (HMDB).

Features:
LC-MS Search Metabolite Matching
    
Instructions for Use:
  1) pip install Selenium and webdriver-manager
  2) If you do not want an automatic install of the chrome web driver, in HMDB_main.py, replace the argument for the Service object assigned      to the service variable with the path to your chrome driver.
  3) To customize the search parameters, first open the HMDB_config.py file.
  4) Update the "option" numerical argument within the XPATH values in the LOCATOR dictionary for the desired parameter.
     * Note: The numerical argument corresponds to the option’s position in HMDB’s dropdown menu.
  5) Once parameters are set, run HMDB_main.py to automatically match m/z inputs to metabolites.
  
