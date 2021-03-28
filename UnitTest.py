import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class UnitTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')

	def test_Buscar(self):
		driver = self.driver
		driver.get("https://www.google.com")
		self.assertIn("Google", driver.title)
		elemento = driver.find_element_by_name("q")
		elemento.send_keys("github")
		elemento.send_keys(Keys.RETURN)
		time.sleep(5)
		#---Verificación del Assert:
		assert "Elemento no encontrado" not in driver.page_source


	def tearDown(self):
		self.driver.close()



if __name__ == '__main__':
	unittest.main()

		