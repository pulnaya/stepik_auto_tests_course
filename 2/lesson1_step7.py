import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	img = browser.find_element(By.CSS_SELECTOR, "#treasure")
	x = img.get_attribute("valuex")
	ans = calc(x)

	input_ans = browser.find_element(By.CSS_SELECTOR, "#answer")
	input_ans.send_keys(ans)
	checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
	checkbox.click()
	radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
	radio_button.click()
	button = browser.find_element(By.CSS_SELECTOR, ".btn")
	button.click()

finally:
	time.sleep(30)
	browser.quit()
