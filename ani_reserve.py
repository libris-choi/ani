import selenium
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Selenium Version : " + selenium.__version__)

options = webdriver.ChromeOptions()
options.add_argument("--window-position=0,0")
options.add_argument("--window-size=1438,925")
options.add_argument("--disable-features=ChromeWhatsNewUI")

# remove "Chrome is being controlled by automated test software" notification
# remove "Disable developer mode extensios" notification
options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

print("Browser Version : " + driver.capabilities['browserVersion'])
print("chrome Driver Version : " +
      driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])

# 날짜변경필요
driver.get('https://')
driver.implicitly_wait(10)
print("page loading complete")

try:
    # room_148 : 일반데크 1
    # room_149 : 일반데크 2
    # room_150 : 일반데크 3
    # room_160 : 일반데크 5
    # room_161 : 일반데크 6
    # room_162 : 일반데크 9
    # room_163 : 일반데크 10
    driver.execute_script("document.querySelector('#room_160').click();")
    driver.execute_script("document.querySelector('#room_161').click();")
    driver.find_element(By.XPATH, '//*[@id="productSelectForm"]/div/div[2]/div[4]/button').click()
except NoSuchElementException:
    None
except JavascriptException:
    # 예약중인경우 강제 종료
    print("input page loading fail")
    time.sleep(3)
    driver.quit()
    sys.exit()

driver.implicitly_wait(10)
print("input page loading complete")

try:
    name = driver.find_element(By.XPATH, '//*[@id="reserv_name"]')
    year = driver.find_element(By.XPATH, '//*[@id="birth_year"]')
    month = driver.find_element(By.XPATH, '//*[@id="birth_month"]')
    day = driver.find_element(By.XPATH, '//*[@id="birth_day"]')
    people = driver.find_element(By.XPATH, '//*[@id="reserv_people"]')
    phone1 = driver.find_element(By.XPATH, '//*[@id="reserv_phone1"]')
    phone2 = driver.find_element(By.XPATH, '//*[@id="reserv_phone2"]')
    phone3 = driver.find_element(By.XPATH, '//*[@id="reserv_phone3"]')

    # 폼입력부분
    name.send_keys('이모씨')
    Select(year).select_by_value('1999')
    Select(month).select_by_value('01')
    Select(day).select_by_value('02')
    Select(people).select_by_value('4')
    Select(phone1).select_by_value('010')
    driver.implicitly_wait(1)
    phone2.send_keys('1000')
    phone3.send_keys('0000')
    driver.implicitly_wait(3)
    print("Form complete")

except NoSuchElementException:
    None

#time.sleep(3600)
#driver.quit()
#sys.exit()
