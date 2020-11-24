from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля            
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Roman")
    
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Miros")
    
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Miros@gmail")
    
    input4 = browser.find_element_by_name('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'vhod.txt')           # добавляем к этому пути имя файла 
    input4.send_keys(file_path)
        
    button = browser.find_element_by_css_selector("button.btn")    
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()