import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	ans = calc(x)

	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(ans)
	check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
	check_box.click()
	radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
	radio_button.click()
	button = browser.find_element(By.CSS_SELECTOR, "button")
	button.click()

finally: 
	time.sleep(30)
	browser.quit()


