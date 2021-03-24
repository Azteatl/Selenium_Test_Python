from selenium import webdriver
import time
from random import randrange

tiempo_vista = 3
lista_navegador = []

n1 = webdriver.Chrome(executable_path='./chromedriver')

n2 = webdriver.Chrome(executable_path='./chromedriver')

lista_navegador.append(n1)
lista_navegador.append(n2)

for navegador in lista_navegador:
	navegador.get('https://www.youtube.com/watch?v=oFnHB7XWygU&ab_channel=Azteatl')
while (True):
	numero_random = randrange(0,len(lista_navegador))
	lista_navegador[numero_random].refresh()
	print('Navegador num. ', numero_random, " se actualizo.")
	time.sleep(tiempo_vista)
"""driver = webdriver.Firefox()

driver.get('https://www.youtube.com/watch?v=oFnHB7XWygU&ab_channel=Azteatl') 
"""
