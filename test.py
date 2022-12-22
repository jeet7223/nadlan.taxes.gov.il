from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
action = ActionChains(driver)
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
time.sleep(10)
driver.find_element(By.XPATH, "//select[@name='ctl00$ContentUsersPage$DDLMahutIska']/option[@value='999']").click()
time.sleep(7)

# Code for Click Search button
driver.find_element(By.ID, "ContentUsersPage_btnHipus").click()
time.sleep(1)
counter = 0
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

driver.find_element(By.ID, 'ContentUsersPage_RadCaptcha1_CaptchaLinkButton').click()
time.sleep(5)
try:
    try:
        img_url = driver.find_element(By.ID, "ContentUsersPage_dialogCaptcha").find_element(By.ID,
                                                                                            "ContentUsersPage_RadCaptcha1_ctl01").find_element(
            By.TAG_NAME, "img").get_attribute("src")
    except:
        img_url = None

    captcha_text = input("Please Enter Captcha :- ")
    time.sleep(2)
    driver.find_element(By.ID, "ContentUsersPage_dialogCaptcha").find_element(By.XPATH,"//input[@id='ContentUsersPage_RadCaptcha1_CaptchaTextBox']").send_keys(captcha_text)
    time.sleep(5)
except:
    pass
# Further Code here

driver.find_element(By.ID, "ContentUsersPage_dialogCaptcha").find_element(By.ID, "ContentUsersPage_btnIshur").click()

try:
    p = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "pageContent")))
    time.sleep(1)
except TimeoutException:
    print("Dont Able to open page")
    driver.quit()
    sys.exit()

# code to do everything

try:
    pages_len = driver.find_element(By.XPATH,'//tr[@class="table_title tabelPages"]//table').find_elements(By.TAG_NAME,'td')
    pages_len = len(pages_len)
except:
    pages_len = 0
print("Total Pages Found -: {}".format(pages_len))
for page_index in range(0, pages_len - 1):
    try:
        table_data = driver.find_element(By.XPATH, '//table[@class="table_title table table-striped table-bordered table-condensed"]').find_elements(By.TAG_NAME, 'tr')
    except:
        table_data = []
    row_len = len(table_data)

    for row_index in range(0, row_len):
        table_item = driver.find_element(By.XPATH, '//table[@class="table_title table table-striped table-bordered table-condensed"]').find_elements(By.TAG_NAME, 'tr')[row_index]
        table_row_class = table_item.get_attribute("class")

        if "row1" in table_row_class or "BoxB" in table_row_class:
            pass
        else:
            continue

        smooth_block = None
        sale_day = None
        declared_return_in_nis = None
        sales_value_in_nis = None
        essence = None
        part_sold = None
        settlement = None
        year_of_construction = None
        area1 = None
        rooms = None
        status = None
        area2 = None
        id_number = None
        date_of_employment = None
        street = None
        house = None
        login = None
        apartment = None
        declare_price_value_in_nis = None
        declare_price_value_in_dollars = None
        estimated_price_value_in_nis = None
        estimated_price_value_in_dollars = None
        property_tax_area = None
        registered_area = None
        price_per_room = None
        price_per_square_meter = None
        number_of_rooms = None
        floor = None
        several_floor = None
        apartments_in_the_building = None
        parking_adjust_to = None
        elevators = None
        roof = None
        storage = None
        yard = None
        court = None
        gallery = None
        transaction_type = None
        the_function_of_building = None
        unit_function = None
        mole_parts = None
        goh_show = None
        according_to_claim = None
        the_essence_of_the_right = None
        try:
            smooth_block = table_item.find_elements(By.TAG_NAME, 'td')[1].text
            sale_day = table_item.find_elements(By.TAG_NAME, 'td')[2].text
            declared_return_in_nis = table_item.find_elements(By.TAG_NAME, 'td')[3].text
            sales_value_in_nis = table_item.find_elements(By.TAG_NAME, 'td')[4].text
            essence = table_item.find_elements(By.TAG_NAME, 'td')[5].text
            part_sold = table_item.find_elements(By.TAG_NAME, 'td')[6].text
            settlement = table_item.find_elements(By.TAG_NAME, 'td')[7].text
            year_of_construction = table_item.find_elements(By.TAG_NAME, 'td')[8].text
            area1 = table_item.find_elements(By.TAG_NAME, 'td')[9].text
            rooms = table_item.find_elements(By.TAG_NAME, 'td')[10].text


            try:
                smooth_block_button = table_item.find_elements(By.TAG_NAME, 'td')[1].find_element(By.TAG_NAME, 'a')
                smooth_block_button.click()
                time.sleep(1)
                status = "Details Found"
                details_found = True
            except:
                status = "Details Not Found"
                details_found = False
            if details_found is True:
                try:
                    p = WebDriverWait(driver, 20).until(
                        expected_conditions.presence_of_element_located((By.ID, "ContentUsersPage_lblEzor")))
                    time.sleep(1)
                except TimeoutException:
                    pass


                try:
                    area2 = driver.find_element(By.CLASS_NAME, "bluediv").find_element(By.ID, "ContentUsersPage_lblEzor").text
                except:
                    pass

                try:
                    id_number = driver.find_element(By.CLASS_NAME, "bluediv").find_element(By.ID, "ContentUsersPage_lblGush").text
                except:
                    pass

                try:
                    date_of_employment = driver.find_element(By.CLASS_NAME, "bluediv").find_element(By.ID, "ContentUsersPage_lblTarIska").text
                except:
                    pass

                try:
                    street = driver.find_element(By.CLASS_NAME, "bluediv").find_element(By.ID, "ContentUsersPage_lblRechov").text
                except:
                    pass

                try:
                    house = driver.find_element(By.CLASS_NAME, "bluediv").find_element(By.ID, "ContentUsersPage_lblBayit").text
                except:
                    pass

                try:
                    login = driver.find_element(By.CLASS_NAME, "bluediv").find_element(By.ID, "ContentUsersPage_lblKnisa").text
                except:
                    pass

                try:
                    apartment = driver.find_element(By.CLASS_NAME, "bluediv").find_element(By.ID, "ContentUsersPage_lblDira").text
                except:
                    pass

                try:
                    declare_price_value_in_nis = driver.find_element(By.ID, "ContentUsersPage_lblMcirMozhar").text
                except:
                    pass

                try:
                    declare_price_value_in_dollars = driver.find_element(By.ID, "ContentUsersPage_lblMcirMozharDlr").text
                except:
                    pass

                try:
                    estimated_price_value_in_nis = driver.find_element(By.ID, "ContentUsersPage_lblMcirMorach").text
                except:
                    pass

                try:
                    estimated_price_value_in_dollars = driver.find_element(By.ID, "ContentUsersPage_lblMcirMorachDlr").text
                except:
                    pass

                try:
                    property_tax_area = driver.find_element(By.ID, "ContentUsersPage_lblShetachBruto").text
                except:
                    pass

                try:
                    registered_area = driver.find_element(By.ID, "ContentUsersPage_lblShetachNeto").text
                except:
                    pass

                # year_of_construction = driver.find_element(By.ID, "ContentUsersPage_lblShnatBniya").text

                try:
                    price_per_room = driver.find_element(By.ID, "ContentUsersPage_lblMechirCheder").text
                except:
                    pass

                try:
                    price_per_square_meter = driver.find_element(By.ID, "ContentUsersPage_lblMechirLmr").text
                except:
                    pass

                try:
                    number_of_rooms = driver.find_element(By.ID, "ContentUsersPage_lblMisHadarim").text
                except:
                    pass

                try:
                    floor = driver.find_element(By.ID, "ContentUsersPage_lblKoma").text
                except:
                    pass

                try:
                    several_floor = driver.find_element(By.ID, "ContentUsersPage_lblMisKomot").text
                except:
                    pass

                try:
                    apartments_in_the_building = driver.find_element(By.ID, "ContentUsersPage_lblDirotBnyn").text
                except:
                    pass

                try:
                    parking_adjust_to = driver.find_element(By.ID, "ContentUsersPage_lblHanaya").text
                except:
                    pass

                try:
                    elevators = driver.find_element(By.ID, "ContentUsersPage_lblMalit").text
                except:
                    pass

                try:
                    roof = driver.find_element(By.ID, "ContentUsersPage_lblGag").text
                except:
                    pass

                try:
                    storage = driver.find_element(By.ID, "ContentUsersPage_lblMachsan").text
                except:
                    pass

                try:
                    yard = driver.find_element(By.ID, "ContentUsersPage_lblHzer").text
                except:
                    pass

                try:
                    court = driver.find_element(By.ID, "ContentUsersPage_lblMigrash").text
                except:
                    pass

                try:
                    gallery = driver.find_element(By.ID, "ContentUsersPage_lblGlrya").text
                except:
                    pass

                try:
                    transaction_type = driver.find_element(By.ID, "ContentUsersPage_lblSugIska").text
                except:
                    pass

                try:
                    the_function_of_building = driver.find_element(By.ID, "ContentUsersPage_lblTifkudBnyn").text
                except:
                    pass

                try:
                    unit_function = driver.find_element(By.ID, "ContentUsersPage_lblTifkudYchida").text
                except:
                    pass

                try:
                    mole_parts = driver.find_element(By.ID, "ContentUsersPage_lblShumaHalakim").text
                except:
                    pass

                try:
                    goh_show = driver.find_element(By.ID, "ContentUsersPage_lblMofaGush").text
                except:
                    pass

                try:
                    according_to_claim = driver.find_element(By.ID, "ContentUsersPage_lblTava").text
                except:
                    pass

                try:
                    the_essence_of_the_right = driver.find_element(By.ID, "ContentUsersPage_lblMahutZchut").text
                except:
                    pass
                driver.back()
                time.sleep(1)
        except:
            pass

        data_set_row = [status, smooth_block, sale_day, declared_return_in_nis, sales_value_in_nis, essence, part_sold, settlement, year_of_construction, area1, rooms, area2, id_number, date_of_employment, street, house, login, apartment, declare_price_value_in_nis, declare_price_value_in_dollars, estimated_price_value_in_nis, estimated_price_value_in_dollars, property_tax_area, registered_area, price_per_room, price_per_square_meter, number_of_rooms, floor, several_floor, apartments_in_the_building, parking_adjust_to, elevators, roof, storage, yard, court, gallery, transaction_type, the_function_of_building, unit_function, mole_parts, goh_show, according_to_claim, the_essence_of_the_right]
        # print(data_set_row)

        # code to enter data in csv
        with open("output.csv", 'a', newline='', encoding="utf8") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data_set_row)
            counter = counter + 1
            print("Data Inserted : {}".format(counter))

    try:
        next_page_button = driver.find_element(By.XPATH, '//tr[@class="table_title tabelPages"]//table').find_elements(By.TAG_NAME, 'td')[page_index + 1].find_element(By.TAG_NAME,'a')
        next_page_button.click()
        time.sleep(2)
        try:
            p = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "pageContent")))
            time.sleep(1)
        except TimeoutException:
            pass
    except:
        print("Not Able to click next page button")

driver.quit()