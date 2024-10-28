from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element(By.ID, "input_value").text
	ans = calc(x)

	input1 = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
	#button.click()
	input1.send_keys(ans)
	check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
	check_box.click()
	radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
	radio_button.click()
	button = browser.find_element(By.CSS_SELECTOR, "button")
	button.click()



finally:
	time.sleep(15)
	browser.quit()
