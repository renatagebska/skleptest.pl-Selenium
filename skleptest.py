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
sortbypricehightolow.click() # need to check sorting as not every works properly

wantedproduct1 = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/ul/li[1]/a[1]')
wantedproduct1.click()
wantedproduct1quantity = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/div/div/input')
wantedproduct1quantity.clear()
wantedproduct1quantity.send_keys(1)
addproduct1 = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/button')
addproduct1.click()
wantedproduct2 = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/ul/li[2]/a[1]')
wantedproduct2.click()
wantedproduct2quantity = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/div/div/input')
wantedproduct2quantity.clear()
wantedproduct2quantity.send_keys(2)
addproduct2 = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/button')
addproduct2.click()
wantedproduct3 = driver.find_element('xpath', '//*[@id="page"]/div/div/div[2]/div/ul/li[3]/a[1]')
wantedproduct3.click()
wantedproduct3quantity = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/div/div/input')
wantedproduct3quantity.clear()
wantedproduct3quantity.send_keys(3)
addproduct3 = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div[2]/form/button')
addproduct3.click()

categories = driver.find_element('id', 'menu-item-123') # need to check for correct spelling - on website is catergies
webdriver.ActionChains(driver).move_to_element(categories).perform()
all = driver.find_element('id', 'menu-item-138')
all.click()
shirts = driver.find_element('id', 'menu-item-125')
shirts.click()
featured = driver.find_element('id', 'menu-item-126')
featured.click()
trends = driver.find_element('id', 'menu-item-127')
trends.click()
scarfs = driver.find_element('id', 'menu-item-129')
scarfs.click()
shoes = driver.find_element('id', 'menu-item-130')
shoes.click()
tops = driver.find_element('id', 'menu-item-131')
tops.click()
blouses = driver.find_element('id', 'menu-item-132') # need to check for correct spelling - on website blouse
blouses.click()
jeans = driver.find_element('id', 'menu-item-134')
jeans.click()
dresses = driver.find_element('id', 'menu-item-133')
dresses.click()

aboutus = driver.find_element('id', 'menu-item-118') # need to check as it redirect to Contact page
aboutus.click()
contact = driver.find_element('id', 'menu-item-108')
contact.click()
blog = driver.find_element('id', 'menu-item-163')
blog.click()


time.sleep(10)
driver.quit()

