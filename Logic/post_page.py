from selenium.common import StaleElementReferenceException
from selenium.common import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PostPage:
    FIRST_COMMENT = "//div[@class='py-0 xs:mx-xs mx-2xs inline-block max-w-full']"
    POST_TITLE = '//h1[@id="post-title-t3_bjxyof"]'
    POST_DESC = '//div[@id="t3_bjxyof-post-rtjson-content"]'

    def __init__(self, driver):
        self.driver = driver
        self.comment_element = self.driver.find_element(By.XPATH, self.FIRST_COMMENT)
        self.post_title_element = self.driver.find_element(By.XPATH, self.POST_TITLE)
        self.post_desc_element = self.driver.find_element(By.XPATH, self.POST_DESC)

    def get_comment_text(self):
        return self.comment_element.text

    def get_post_title(self):
        return self.post_title_element.text

    def get_post_desc(self):
        return self.post_desc_element.text