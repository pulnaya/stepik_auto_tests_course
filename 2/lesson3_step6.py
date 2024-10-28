from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button1 = browser.find_element(By.CSS_SELECTOR, ".btn").click()
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	x = browser.find_element(By.ID, "input_value").text
	ans = calc(x)
	input1 = browser.find_element(By.ID, "answer").send_keys(ans)
	button2 = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
	time.sleep(15)
	browser.quit()

