from selenium.common import StaleElementReferenceException
from selenium.common import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PostPage:

    COMMENT = "//div[@class='py-0 xs:mx-xs mx-2xs inline-block max-w-full']"

    def __init__(self, driver):
        self.driver = driver
        self.comment_element = self.driver.find_element(By.XPATH,"//div[@class='py-0 xs:mx-xs mx-2xs inline-block max-w-full']")

    def get_comment_text(self):
        return self.comment_element.text
