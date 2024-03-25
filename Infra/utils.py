import json

from dotenv import load_dotenv
import os

class Utils:
    def __init__(self):
        load_dotenv()

    def get_client_id(self):
        return os.getenv("CLIENT_ID")

    def get_client_secret(self):
        return os.getenv("CLIENT_SECRET")

    def get_username(self):
        return os.getenv("USERNAME")

    def get_password(self):
        return os.getenv("PASSWORD")

    def get_user_agent(self):
        return os.getenv("USER-AGENT")

    def get_config_file(self):
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        return config_data

    def get_subreddit_url(self, config_data):
        subreddit_url = config_data.get("subredditURl")
        return subreddit_url

    def get_subreddit_name(self, config_data):
        subreddit_name = config_data.get("subredditName")
        return subreddit_name

# Example usage:
if __name__ == "__main__":
    utils = Utils()
    client_id = utils.get_client_id()
    client_secret = utils.get_client_secret()
    username = utils.get_username()
    password = utils.get_password()
    user_agent = utils.get_user_agent()

    print("Client ID:", client_id)
    print("Client Secret:", client_secret)
    print("Username:", username)
    print("Password:", password)
    print("User Agent:", user_agent)

    config_data = utils.get_config_file()
    subreddit_url = utils.get_subreddit_url(config_data)
    subreddit_name = utils.get_subreddit_name(config_data)

    print("Subreddit URL:", subreddit_url)
    print("Subreddit Name:", subreddit_name)
