import json
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BrowserWrapper:


    def __init__(self):
        self.driver = None
        self.json = self.get_json_file()
        print('test has started')

    def get_json_file(self):
        # Get the absolute path of the config.json file
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.json"))

        try:
            with open(file_path, "r") as f:
                config = json.load(f)
            return config
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {file_path}")
            return None


    def get_hub_url(self):
        return self.json["hub"]

    def get_is_parallel(self):
        return self.json["parallel"]


    def get_driver(self, browser="chrome",website_url=""):
        grid = self.json["grid"]
        url_hub = self.get_hub_url()

        if grid:
            options = self.get_cap_list()
            self.driver = webdriver.Remote(command_executor=url_hub, options=options)

        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()

        self.driver.get(website_url)
        return self.driver

    def set_url_for_driver(self, website_url):
        self.driver.get(website_url)

    def get_cap_list(self):
        self.json_config = self.get_json_file()

        if "capabilities" not in self.json_config:
            raise ValueError("Missing 'capabilities' configuration in config.json")

        for browser in self.json_config["capabilities"]:
            if browser["browserName"] == "chrome":
                self.options_chrome = webdriver.ChromeOptions()
                self.options_chrome.add_argument('--platform=Windows 11')

            elif browser["browserName"] == "firefox":
                self.options_firefox = webdriver.FirefoxOptions()
                self.options_firefox.add_argument('--platform=Windows 11')

            else:
                raise ValueError(f"Unsupported browser: {browser['browserName']}")

        cap_list = [self.options_chrome, self.options_firefox]
        print(cap_list)
        return cap_list

    def get_browser_names(self):
        try:
            # Load JSON data
            data = self.get_json_file()

            # Initialize a list to store browser names
            browser_names = []

            # Iterate through each capability dictionary
            for capability in data.get("capabilities", []):
                # Extract browserName from each capability and append to the list
                browser_name = capability.get("browserName")
                if browser_name:
                    browser_names.append(browser_name)

            return browser_names

        except json.JSONDecodeError:
            print("Invalid JSON format")
            return []

    def get_teardown(self):
        self.driver.quit()
