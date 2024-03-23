import selenium
import praw
from selenium import webdriver
from selenium.webdriver.common.by import By

from Infra.browser_wrapper import BrowserWrapper

# Sign in to Reddit using PRAW

    # Access Reddit using Selenium
def access_reddit():
    driver = webdriver.Chrome()  # Replace this with the appropriate WebDriver for your browser
    driver.get("https://www.reddit.com/r/QAutomation/comments/1biuyuz/test_collections_post_1/")
    return driver

# Main function
def main():
    driver = access_reddit()

    comment_element = driver.find_element(By.XPATH, "//div[@class='py-0 xs:mx-xs mx-2xs inline-block max-w-full']")
    comment_text = comment_element.text

    print("Comment Text:", comment_text)

    # Close the browser window
    driver.quit()


if __name__ == '__main__':
        main()
