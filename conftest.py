import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from settings import *



@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless(True)
    chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture
def driver_friends_chrome(request):
    driver = webdriver.Chrome()
    driver.get('https://petfriends.skillfactory.ru/login')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(valid_email)
    driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(valid_password)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                           'button[type="submit"]')))
    driver.find_element(By.XPATH, '//body/div[1]/div[1]/form[1]/div[3]/button[1]').submit()
    return driver

    driver.quit()