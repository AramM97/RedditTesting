import unittest
import concurrent.futures

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper

from Logic.subreddit_logic import SubReddit
from Logic.post_page import PostPage

class TestCollection(unittest.TestCase):

    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.reddit = self.api_wrapper.sign_in_to_reddit()
        self.subReddit = SubReddit(self.reddit)
        self.browser = BrowserWrapper()
        self.cap_list = self.browser.get_cap_list()


    def test_run_grid_serial(self):
        for cap in self.cap_list:
            self.test_comment_on_post(cap)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_comment_on_post, self.cap_list)


    def test_comment_on_post(self, cap):
        post_url = 'https://www.reddit.com/r/QAutomation/comments/1biuyuz/test_collections_post_1/'

        self.driver = self.browser.get_driver(cap, website_url=post_url)
        self.post_page = PostPage(self.driver)

        # test multiple languages such as arabic english hebrew
        comment_text_api = "comment posting test"
        self.subReddit.post_comment(post_url, comment_text_api)

        self.comment_text = self.post_page.get_comment_text()

        print("Comment Text:", self.comment_text)
        self.assertIn(comment_text_api, self.comment_text, "comment is not working")
        self.driver.quit()
        return

    def tearDown(self) -> None:

        return