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
