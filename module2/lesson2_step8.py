from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

#Заполнение полей
first_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
first_name.send_keys("I")
last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')
last_name.send_keys("P")
email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter email"]')
email.send_keys("S")

#Загрузка файла
upload_file = browser.find_element(By.CSS_SELECTOR, "input[accept='.txt']")
import os 
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
upload_file.send_keys(file_path)

#Нажать на кнопку
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(20)
# закрываем браузер после всех манипуляций
browser.quit()