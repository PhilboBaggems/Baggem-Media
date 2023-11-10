from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def for_posts(driver, hashtag):
    explore_button = driver.find_element(By.XPATH, "//span[contains(.,'Explore')]")
    explore_button.click()
    time.sleep(2)
    search_bar = driver.find_element(By.CSS_SELECTOR, '.r-30o5oe')
    search_bar.send_keys(hashtag)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)
    latest_button = driver.find_element(By.CSS_SELECTOR, '.css-1dbjc4n:nth-child(2) > .css-4rbku5 .css-901oao > .css-901oao')
    latest_button.click()
    time.sleep(2)
    # post_1_comment_button = driver.find_element(By.CLASS_NAME, 'css-1dbjc4n r-xoduu5')
    comment_icon = driver.find_element(By.CSS_SELECTOR, 'css-1dbjc4n r-xoduu5')
    comment_icon.click()
    time.sleep(200)
