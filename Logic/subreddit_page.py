
from selenium.webdriver.common.by import By

class SubredditPage:

    SUB_TITLE = '//h1[@class="flex items-center font-bold text-18 xs:text-32 mb-0"]'

    def __init__(self, driver):
        self.driver = driver
        self.sub_title_element = self.driver.find_element(By.XPATH, self.SUB_TITLE)

    def get_sub_title(self):
        return self.sub_title_element.text
