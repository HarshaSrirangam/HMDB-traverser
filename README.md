# **HMDB Traverser**

This is a Python-based software that automates mass spectrometry data to metabolite matching via scraping the Human Metabolome Database (HMDB).

## **Requirements**
- Latest version of Python 
- Selenium and webdriver-manager installed via pip
- Latest version of Google Chrome, Firefox, or Microsoft Edge

## **Instructions to Use**
1. Download all files from this folder.
2. Adjust search parameters to your liking by editing the `SEARCH_PARAMS` dictionary in `config.py` (change the values of the key corresponding to the parameter you wish to set).
   - Note: This version of HMDB Traverser only supports LC-MS searching.
3. Once search parameters are set, run `main.py`.
