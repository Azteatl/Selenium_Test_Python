import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Unitest(unittest.TestCase):

""" Un Xpath es 1 estructura de direcciones, carpetas,
objetos similares a nuestro árbol de direcciones 
de nuestro disco C:\\

Hay Relativo(parte de 1 módulo o nodo específico) busca 
a partir del nodo del cual le indiquemos buscando en todo 
el árbol de direcciones donde lo encuentre. Es altamente
recomendable usarlo.


El absoluto es toda la ruta completa, no busca en ningún 
otro lugar ni dirección ni carpeta que le indiquemos."""

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')

	def testXPath(self):
		driver =self.driver
		driver.get("https://www.Google.com")
		time.sleep(5)
		#---Buscamos con XPATH Reativo:
		buscando_por_XPath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
		time.sleep(5)
		buscando_por_XPath.send_keys("selenium", Keys.ARROW_DOWN)
		time.sleep(5)


	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':
	unittest.main()





