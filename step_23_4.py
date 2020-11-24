from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os 

def calc(x):
    return str(math.log(abs(12*math.sin(x))))
    
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")    
    button.click()     
  
    confirm = browser.switch_to.alert
    confirm.accept()  
    
    # Ваш код, который заполняет обязательные поля   

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    s=calc(int(x))
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(s)
    
    button2 = browser.find_element_by_css_selector("button.btn")    
    button2.click()     
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()