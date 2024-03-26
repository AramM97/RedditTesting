# test reddit post title limit of 300 check negative test of title post of over 300

import unittest
import concurrent.futures

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Infra.utils import Utils

from Logic.subreddit_logic import SubReddit
from Logic.post_page import PostPage
from Logic.subreddit_page import SubredditPage


class TestCollection(unittest.TestCase):

    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.reddit = self.api_wrapper.sign_in_to_reddit()
        self.subReddit = SubReddit(self.reddit)
        self.browser = BrowserWrapper()
        self.cap_list = self.browser.get_cap_list()
        self.utils = Utils


    def test_run_grid_serial(self):
        for cap in self.cap_list:
            self.test_post_comment_workflow(cap)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_post_comment_workflow, self.cap_list)


    def test_post_on_subreddit(self, cap, limit = 50):
        sub_url = self.utils.get_subreddit_url()
        sub_name = self.utils.get_subreddit_name()
        self.driver = self.browser.get_driver(cap, website_url=sub_url)
        self.post_page = PostPage(self.driver)

        # test the limit
        post_title = self.utils.generate_post_title(limit)

        # test multiple languages such as english and hebrew
        post_desc = self.utils.generate_random_comment()

        self.subReddit.create_post(sub_name, post_title, post_desc)

        # get the post title and desc
        self.title_text = self.post_page.get_post_title()
        self.desc_text = self.post_page.get_post_desc()

        self.assertIn(post_title, self.title_text, "title is not working")
        self.assertIn(post_desc, self.desc_text, "desc is not working")
        self.driver.quit()
        return

    def test_post_comment_workflow(self, cap):
        post_url, post_title, post_desc, comment = self.subReddit.post_and_comment_workflow()

        self.driver = self.browser.get_driver(cap, website_url=post_url)
        self.post_page = PostPage(self.driver)

        # get the post title and desc
        self.title_text = self.post_page.get_post_title()
        self.desc_text = self.post_page.get_post_desc()

        self.assertIn(post_title, self.title_text, "title is not working")
        self.assertIn(post_desc, self.desc_text, "desc is not working")

        self.driver.quit()

    def tearDown(self) -> None:
        return