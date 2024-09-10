from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

#Кнопка book
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element(By.CSS_SELECTOR, '#book')
button.click()

#Скролл вниз
input = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)

#Решение задачи
num = browser.find_element(By.CSS_SELECTOR, "span[id ='input_value']")
x = num.text
total = str(log(abs(12*sin(int(x)))))
input = browser.find_element(By.CSS_SELECTOR, "input[id = 'answer']")
input.send_keys(total)

#Кнопка submit
submit = browser.find_element(By.CSS_SELECTOR, '#solve').click()

time.sleep(20)
# закрываем браузер после всех манипуляций
browser.quit()