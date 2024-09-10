from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

#Кнопка
button = browser.find_element(By.CSS_SELECTOR, '.btn').click()

#Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

#Решение задачи
num = browser.find_element(By.CSS_SELECTOR, "span[id ='input_value']")
x = num.text
total = str(log(abs(12*sin(int(x)))))
input = browser.find_element(By.CSS_SELECTOR, "input[id = 'answer']")
input.send_keys(total)

#Кнопка submit
submit = browser.find_element(By.CSS_SELECTOR, '.btn').click()

time.sleep(20)
# закрываем браузер после всех манипуляций
browser.quit()
