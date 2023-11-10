from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import getpass

def initialize_chrome_webdriver():
    chrome_webdriver_path = os.path.join('drivers', 'chromedriver-win64', 'chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-data-dir=C:\\Users\\bbdnet2843\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2')
    chrome_service = Service(chrome_webdriver_path)
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    driver.implicitly_wait(30)
    return driver

def prompt_user_google_email_address():
    email = input("Enter your google email address: ")
    return email

def prompt_user_for_google_password():
    password = getpass.getpass("Enter your Google account password: ")
    return password

def initialize_script(driver):
    driver.get('https://twitter.com')