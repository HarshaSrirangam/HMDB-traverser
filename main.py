from scraper import primary_search, tolerance_search, dynamic_search, traverse_candidates, get_number_of_entries
from utils import results
from driver_setup import initialize_headed_driver, initialize_headless_driver, quit_driver


if __name__ == '__main__':
    try:
<<<<<<< HEAD
        current_driver = initialize_headless_driver() # initialize driver
=======
        current_driver = initialize_headless_driver() # initialize driver
>>>>>>> 363d3478d27657c435c3811762b02d6efb49c562
        entries = primary_search(current_driver) # search for compounds
        dynamic_search(current_driver, entries) # if primary search yields too many compounds, keep adjusting tolerance until number of compounds is within range
        initial_candidates = traverse_candidates(current_driver) # once number of compounds is within range, extract compound info
        results(initial_candidates) # filter compounds by detection status and present final compounds
    except Exception as e:
        print(e)
    finally:
<<<<<<< HEAD
        quit_driver(current_driver) # quit driver
=======
        quit_driver(current_driver) # quit driver
>>>>>>> 363d3478d27657c435c3811762b02d6efb49c562
