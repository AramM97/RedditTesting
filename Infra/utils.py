import json
import random
from faker import Faker

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

    def generate_random_comment(self):
        # Initialize Faker for English and Hebrew
        faker_en = Faker(['en_US'])
        faker_he = Faker(['he_IL'])

        # Choose randomly between English and Hebrew
        language_choice = random.choice(['English', 'Hebrew'])

        # Generate random passage based on chosen language
        if language_choice == 'English':
            english_passage = faker_en.paragraph()
            print("English Passage:")
            print(english_passage)
            return english_passage
        else:
            hebrew_passage = faker_he.paragraph()
            print("Hebrew Passage:")
            print(hebrew_passage)
            return hebrew_passage

    def generate_post_title(self, max_length, language='both'):
        # Initialize Faker for English and Hebrew
        faker_en = Faker(['en_US'])
        faker_he = Faker(['he_IL'])

        # Choose randomly between English and Hebrew if 'both' is selected
        if language == 'both':
            language = random.choice(['English', 'Hebrew'])

        # Generate random title based on chosen language
        if language == 'English':
            post_title = faker_en.text(max_nb_chars=max_length)
        else:
            post_title = faker_he.text(max_nb_chars=max_length)

        return post_title


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

    max_title_length = 350  # Adjust the max length as per your requirement
    post_title = utils.generate_post_title(max_title_length)
    print("Post Title:")
    print(post_title)