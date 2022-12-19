import csv
import random
import string
import sys
import time
import warnings

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import configuration

warnings.filterwarnings("ignore")

options = webdriver.ChromeOptions()
if configuration.headless_mode:
    options.add_argument('--headless')



driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser = driver
counter = 1

driver.get(
    "https://nadlan.taxes.gov.il/svinfonadlan2010/startpageNadlanNewDesign.aspx?ProcessKey=e0fcc9b4-de6f-47a3-8b26-b36cb1fb13ed")
driver.maximize_window()
try:
    p = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "frame")))
    time.sleep(2)
except TimeoutException:
    print("Dont Able to open page")
    driver.quit()
    sys.exit()

# Code for Filling Inputs

driver.find_element(By.CLASS_NAME, "mainContent").find_element(By.ID, "rbMegush").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, "mainContent").find_element(By.ID, "txtmegusha").send_keys("7103")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "mainContent").find_element(By.ID, "txthelka").send_keys("1")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "mainContent").find_element(By.ID, "txtadGush").send_keys("7103")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "mainContent").find_element(By.ID, "txtadHelka").send_keys("10")
time.sleep(1)
driver.find_element(By.XPATH, "//select[@name='ctl00$ContentUsersPage$DDLTypeNehes']/option[@value='1']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//select[@name='ctl00$ContentUsersPage$DDLMahutIska']/option[@value='999']").click()
time.sleep(3)

# Code for Click Search button
driver.find_element(By.ID, "ContentUsersPage_btnHipus").click()
time.sleep(1)

# Code for Captcha Actions
try:
    p = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.ID, "ContentUsersPage_dialogCaptcha")))
    time.sleep(3)
except TimeoutException:
    print("Not able to See captcha")
    driver.quit()
    sys.exit()
correct = 1

driver.find_element(By.ID,'ContentUsersPage_RadCaptcha1_CaptchaLinkButton').click()
time.sleep(5)
try:
    try:
        img_url = driver.find_element(By.ID, "ContentUsersPage_dialogCaptcha").find_element(By.ID,
                                                                                            "ContentUsersPage_RadCaptcha1_ctl01").find_element(
            By.TAG_NAME, "img").get_attribute("src")
    except:
        img_url = None


    captcha_text = input("Please Enter Captchas")
    driver.find_element(By.ID, "ContentUsersPage_dialogCaptcha").find_element(By.XPATH,"//input[@id='ContentUsersPage_RadCaptcha1_CaptchaTextBox']").send_keys(captcha_text)
    time.sleep(3)
except:
    pass


#Further Code here
driver.quit()