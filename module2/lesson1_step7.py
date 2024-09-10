from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = 'https://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)
    
x_element = browser.find_element(By.CSS_SELECTOR, 'h2 > [valuex]')
x_valuex = x_element.get_attribute("valuex")
x = x_valuex
y = str(math.log(abs(12*math.sin(int(x)))))

input = browser.find_element(By.CSS_SELECTOR, '#answer')
input.send_keys(y)

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, 'robotsRule')
radio.click()

button = browser.find_element(By.CSS_SELECTOR, ".btn")
button.click()

time.sleep(1)

time.sleep(20)
browser.quit()