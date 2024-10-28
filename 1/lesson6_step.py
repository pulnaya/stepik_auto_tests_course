from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_form = browser.find_element(By.XPATH, "//div[1]/div[@class='form-group first_class']/input")
    first_form.send_keys('1')

    second_form = browser.find_element(By.XPATH, "//div[1]/div[@class='form-group second_class']/input")
    second_form.send_keys('2')

    third_form = browser.find_element(By.XPATH, "//div[1]/div[@class='form-group third_class']/input")
    third_form.send_keys('3')
    
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(10)
    browser.quit()