from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://skleptest.pl/')

account = driver.find_element('xpath', '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a')
account.click()
reg_email = driver.find_element(By.CSS_SELECTOR, 'input#reg_email')
reg_email.click()
reg_email.send_keys('reg.email@spoko.pl')
reg_password = driver.find_element(By.CSS_SELECTOR, 'input#reg_password')
reg_password.click()
reg_password.send_keys('RegPassword1!')
reg_button = driver.find_element('xpath', '//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')
reg_button.click()


time.sleep(10)
driver.quit()