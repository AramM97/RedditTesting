import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Logic.subreddit_logic import SubReddit

class TestCollection(unittest.TestCase):

    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.reddit = self.api_wrapper.sign_in_to_reddit()
        self.subReddit = SubReddit(self.reddit)
        #self.browser = BrowserWrapper()
        self.driver = webdriver.Chrome()


    def test_comment_on_post(self):
        post_url = 'https://www.reddit.com/r/QAutomation/comments/1biuyuz/test_collections_post_1/'
        comment_text_api = "comment posting test."
        self.subReddit.post_comment(post_url, comment_text_api)
        self.driver.get(post_url)
        comment_element = self.driver.find_element(By.XPATH, "//div[@class='py-0 xs:mx-xs mx-2xs inline-block max-w-full']")
        comment_text = comment_element.text

        print("Comment Text:", comment_text)
        self.assertEqual(comment_text_api,comment_text,"comment is not working")
        return

    def tearDown(self) -> None:
        self.driver.quit()
        return