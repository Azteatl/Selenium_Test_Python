import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class UnitTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')

	def test_Cambiar_Ventana(self):
		driver = self.driver
		driver.get("https://www.google.com")
		time.sleep(5)
		#---Indicamos apertura de nva. pestaña mediante script de Python:
		driver.execute_script("window.open('');")
		time.sleep(5)
		#---Indicamos posicionamiento en nva ventana y le pasamos la direccion web:
		driver.switch_to.window(driver.window_handles[1])
		driver.get("https://stackoverflow.com")
		time.sleep(5)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(3)


if __name__ == '__main__':
	unittest.main()