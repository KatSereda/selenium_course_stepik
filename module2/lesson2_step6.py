from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import * 

link = 'https://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)
    
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value') #Считать значение для переменной x
x = x_element.text
y = str(log(abs(12*sin(int(x))))) #Посчитать математическую функцию от x

input = browser.find_element(By.ID, "answer") #Проскроллить страницу вниз
browser.execute_script("return arguments[0].scrollIntoView(true);", input)

input = browser.find_element(By.CSS_SELECTOR, '#answer') #Ввести ответ в текстовое поле
input.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]') #Выбрать checkbox "I'm the robot"
checkbox.click()
radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]') #Переключить radiobutton "Robots rule!"
radio.click()

button = browser.find_element(By.CSS_SELECTOR, ".btn") #Нажать на кнопку "Submit"
button.click()

time.sleep(1)

time.sleep(20)
browser.quit()