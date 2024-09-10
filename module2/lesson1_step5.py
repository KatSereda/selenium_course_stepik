from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)
    
x_element = browser.find_element(By.CSS_SELECTOR, 'label > #input_value')
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))

input = browser.find_element(By.CSS_SELECTOR, '#answer')
input.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
checkbox.click()
radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
radio.click()

button = browser.find_element(By.CSS_SELECTOR, ".btn")
button.click()

time.sleep(1)

time.sleep(20)
browser.quit()