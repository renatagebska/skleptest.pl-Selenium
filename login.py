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
login = driver.find_element(By.CSS_SELECTOR, 'input#username')
login.click()
login.send_keys('reg.email@spoko.pl')
password = driver.find_element(By.CSS_SELECTOR, 'input#password')
password.click()
password.send_keys('RegPassword1!')
login_button = driver.find_element('xpath', '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
login_button.click()
log_out = driver.find_element('xpath', '//*[@id="post-8"]/div[2]/div/p[1]/a')
log_out.click()

time.sleep(10)
driver.quit()