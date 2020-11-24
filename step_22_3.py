from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x,y):
    return str(x+y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id('num1')
    x = x_element.text
    print(x)
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    print(y)
    s=calc(int(x),int(y))
    print(s)
    sum=str(s)   
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s) # ищем элемент с текстом "Python"
    
    input2 = browser.find_element_by_css_selector("button.btn")
    input2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()