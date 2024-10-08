from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
    
num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
x = num1.text
num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
y = num2.text
summa = int(x) + int(y)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(summa))

button = browser.find_element(By.CSS_SELECTOR, ".btn")
button.click()

time.sleep(5)
browser.quit()