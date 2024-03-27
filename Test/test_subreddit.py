# test reddit post title limit of 300 check negative test of title post of over 300

import unittest
import concurrent.futures

import sys
import os

# Add the project directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Infra.utils import Utils

from Logic.subreddit_logic import SubReddit
from Logic.post_page import PostPage
from Logic.subreddit_page import SubredditPage

from jira_report import JiraReport

class TestSubreddit(unittest.TestCase):
    def setUp(self) -> None:
        self.api_wrapper = APIWrapper()
        self.reddit = self.api_wrapper.sign_in_to_reddit()
        self.subReddit = SubReddit(self.reddit)
        self.utils = Utils()
        self.sub_url = self.utils.get_subreddit_url()
        self.sub_name = self.utils.get_subreddit_name()

    def test_get_top_subreddits(self):

        #top_subreddits = self.subReddit.get_top_subreddits_according_to_location()
        top_subreddits = self.subReddit.get_sub_count("testingground4bots")

        self.assertIsNotNone(top_subreddits)


    def tearDown(self) -> None:
        # Check if the last test method succeeded
        if not self._outcome.success:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_subreddit"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))