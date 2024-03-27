import os

from dotenv import load_dotenv

class GeneralUtils:

    def __init__(self):
        load_dotenv()
        self.jira_token = os.getenv("JIRATOKEN")
        self.jira_domain = os.getenv("JIRADOMAIN")
        self.jira_email = os.getenv("EMAIL")
        self.jira_key = os.getenv("KEY")

    def get_jira_token(self):
        # Get the Jira token.
        return self.jira_token

    def get_jira_domain(self):
        # Get the Jira domain.
        return self.jira_domain

    def get_jira_email(self):
        # Get the Jira email.
        return self.jira_email

    def get_jira_key(self):
        # Get the Jira email.
        return self.jira_key