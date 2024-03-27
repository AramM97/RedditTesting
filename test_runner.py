import unittest
from concurrent.futures import ThreadPoolExecutor
from typing import Type

# Import the test class containing test cases
from Test.test_comments import TestComments
from Test.test_post import TestPost

from Infra.browser_wrapper import BrowserWrapper

# load test cases
serial_cases = [TestPost]
parallel_cases = [TestPost]
demo_cases = [TestPost]

# tests call
def run_tests_for_browser(browser: str, test_case: Type[unittest.TestCase]):
    test_case.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner().run(test_suite)

# serial run
def run_tests_for_browser_serial(cap_list, serial_tests):
    for test in serial_tests:
        for cap in cap_list:
            run_tests_for_browser(cap, test)

# parallel run
def run_tests_for_browser_parallel(cap_list, parallel_tests):
    tasks = [(cap, test_case) for cap in cap_list for test_case in parallel_tests]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(run_tests_for_browser, cap, test_case) for cap, test_case in tasks]


if __name__ == "__main__":
    browser = BrowserWrapper()
    cap_list = browser.get_cap_list()

    is_parallel = browser.get_is_parallel()
    is_serial = not browser.get_is_parallel()

    browsers = browser.get_browser_names()
    grid_url = browser.get_hub_url()
    if is_parallel:
        run_tests_for_browser_parallel(cap_list, parallel_cases)
    elif is_serial:
        run_tests_for_browser_serial(cap_list, serial_cases)
    else:
        run_tests_for_browser_serial(cap_list, demo_cases)