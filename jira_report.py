from jira import JIRA

from Utils.general_utils import GeneralUtils

class JiraReport:
    def __init__(self):
        self.general_utils = GeneralUtils()
        self.jira_token = self.general_utils.get_jira_token()
        self.jira_url = self.general_utils.get_jira_domain()
        self.jira_email = self.general_utils.get_jira_email()
        self.jira_project_key = self.general_utils.get_jira_key()
        self.auth_jira = JIRA(basic_auth=(self.jira_email, self.jira_token), options={'server': self.jira_url})

    def create_issue(self, summery, description, issue_type="Bug"):
        issue_dict = {
            'project': {'key': self.jira_project_key},
            'summary': f'failed test: {summery}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key

'''
        if hasattr(self, 'assertion_passed') and self.assertion_passed:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_create_board" ..
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))
'''