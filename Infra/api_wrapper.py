import requests
import praw
import os

from dotenv import load_dotenv


class APIWrapper:


    def __init__(self):
        self.response = None
        self.my_request = requests
        load_dotenv()
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER-AGENT")
        self.username = os.getenv("REDDIT_USER")
        self.password = os.getenv("REDDIT_PASSWORD")

    def sign_in_to_reddit(self):
        reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            username=self.username,
            password=self.password
        )

        print(reddit.user.me())
        return reddit

    def api_get_request(self, url):
        self.token = self.get_token()
        self.headers = self.get_auth_header(self.token)
        self.response = self.my_request.get(url, headers= self.headers)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, url , token):
        self.headers = self.get_auth_header(token)
        self.response = self.my_request.post(url, headers=self.headers)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code


