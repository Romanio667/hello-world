from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    s=calc(int(x))
            
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(s)
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click() 
    
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)   
    
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click() 
    
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()