import time

from selenium.common import StaleElementReferenceException
from selenium.common import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PostPage:
    POST_TITLE = '//h1[@class="font-semibold text-neutral-content-strong m-0 text-18 xs:text-24  mb-xs px-md xs:px-0 xs:mb-md "]'
    POST_DESC = '//div[@class="text-neutral-content"]/div/div'

    def __init__(self, driver):
        self.driver = driver
        self.post_title_element = self.driver.find_element(By.XPATH, self.POST_TITLE)
        self.post_desc_element = self.driver.find_element(By.XPATH, self.POST_DESC)


    def get_post_title(self):
        return self.post_title_element.text

    def get_post_desc(self):
        return self.post_desc_element.text