import unittest

from Infra.browser_wrapper import BrowserWrapper

class TestCollection(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = BrowserWrapper()


    def test_collection(self):
        driver = self.browser.get_driver("")
        return

    def tearDown(self) -> None:
        return