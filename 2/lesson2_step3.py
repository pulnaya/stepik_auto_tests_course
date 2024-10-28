from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#link = "https://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	num1 = browser.find_element(By.ID, "num1").text
	num2 = browser.find_element(By.ID, "num2").text
	ans = int(num1) + int(num2)

	select = Select(browser.find_element(By.TAG_NAME, "select"))
	select.select_by_visible_text(str(ans))

	button = browser.find_element(By.TAG_NAME, "button").click()

finally:
	time.sleep(20)
	browser.quit()


