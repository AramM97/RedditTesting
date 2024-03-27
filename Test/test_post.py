# test reddit post title limit of 300 check negative test of title post of over 300

import unittest
import concurrent.futures

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Infra.utils import Utils

from Logic.subreddit_logic import SubReddit
from Logic.post_page import PostPage
from Logic.subreddit_page import SubredditPage

from jira_report import JiraReport


class TestPost(unittest.TestCase):

    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.reddit = self.api_wrapper.sign_in_to_reddit()
        self.subReddit = SubReddit(self.reddit)
        self.browser = BrowserWrapper()
        self.cap_list = self.browser.get_cap_list()
        self.utils = Utils()
        self.sub_url = self.utils.get_subreddit_url()
        self.sub_name = self.utils.get_subreddit_name()
        self.driver = self.browser.get_driver(website_url=self.sub_url)

    def test_post_on_subreddit(self, limit=50):


        # test the limit
        post_title = self.utils.generate_post_title(limit)

        # test multiple languages such as english and hebrew
        post_desc = self.utils.generate_random_comment()

        post_url = self.subReddit.create_post(self.sub_name, post_title, post_desc)

        self.browser.set_url_for_driver(post_url)
        self.post_page = PostPage(self.driver)


        # get the post title and desc
        self.title_text = self.post_page.get_post_title()
        self.desc_text = self.post_page.get_post_desc()

        self.assertIn(post_title, self.title_text, "title is not working")
        self.assertIn(post_desc, self.desc_text, "desc is not working")

    def test_post_comment_workflow(self):
        post_url, post_title, post_desc, comment = self.subReddit.post_and_comment_workflow()

        self.driver = self.browser.get_driver(website_url=post_url)
        self.post_page = PostPage(self.driver)

        # get the post title and desc
        self.title_text = self.post_page.get_post_title()
        self.desc_text = self.post_page.get_post_desc()

        self.assertIn(post_title, self.title_text, "title is not working")
        self.assertIn(post_desc, self.desc_text, "desc is not working")

    def tearDown(self) -> None:
        self.driver.quit()
        if hasattr(self, 'assertion_passed') and self.assertion_passed:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_create_board"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))
        return
