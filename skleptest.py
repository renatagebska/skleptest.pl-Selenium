from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://skleptest.pl/')

mostwanted = driver.find_element('id', 'menu-item-128')
mostwanted.click()

results = driver.find_element('name', 'orderby')
results.click()
defaultsorting = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/form/select/option[1]')
sortbypopularity = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/form/select/option[2]')
sortbypopularity.click()
sortbyrating = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/form/select/option[3]')
sortbyrating.click()
sortbynewness = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/form/select/option[4]')
sortbynewness.click()
sortbypricelowtohigh = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/form/select/option[5]')
sortbypricelowtohigh.click()
sortbypricehightolow = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/form/select/option[6]')
sortbypricehightolow.click()

# wantedproduct1 = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/ul/li[1]/a[1]')
# wantedproduct1.click()
# wantedproduct1quantity = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/div/div/input')
# wantedproduct1quantity.clear()
# wantedproduct1quantity.send_keys(1)
# addproduct1 = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/button')
# addproduct1.click()
# wantedproduct2 = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/ul/li[2]/a[1]')
# wantedproduct2.click()
# wantedproduct2quantity = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/div/div/input')
# wantedproduct2quantity.clear()
# wantedproduct2quantity.send_keys(2)
# addproduct2 = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/button')
# addproduct2.click()
wantedproduct3 = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/ul/li[3]/a[1]')
wantedproduct3.click()
wantedproduct3quantity = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/div/div/input')
wantedproduct3quantity.clear()
wantedproduct3quantity.send_keys(3)
addproduct3 = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/button')
addproduct3.click()

time.sleep(10)
driver.quit()