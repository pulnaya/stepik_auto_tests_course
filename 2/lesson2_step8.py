import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
os.path.abspath(__file__) # путь к испольняемому файлу
print(os.path.abspath(os.path.dirname(__file__))) #путь к директории текущего исполняемого файла 

#Загрузка файла в форму
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)

'''
link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element(By.NAME, "firstname").send_keys("Ivan")
	input2 = browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
	input3 = browser.find_element(By.NAME, "email").send_keys("my_email@mail.com")

	current_dir = os.path.abspath(os.path.dirname(__file__)) 
	file_path = os.path.join(current_dir, 'file.txt') 
	input4 = browser.find_element(By.ID, "file").send_keys(file_path)

	buttom = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
	time.sleep(15)
	browser.quit()