from selenium import webdriver
#Llamadas a teclado:
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://gmail.com")

user = driver.find_element_by_id("identifierId")
user.send_keys("myEmail")
user.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("xxxxxxx")
clave.send_keys(Keys.ENTER)

driver.close()