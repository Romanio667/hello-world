from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("h2 > img")
    x_element_ch = x_element.get_attribute("valuex")
    x = x_element_ch
    y = calc(x)
    input1 = browser.find_element_by_css_selector("[type='text']")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_id('robotCheckbox')
    option1_1 = option1.get_attribute("required")
    option1.click() 
    
    option2 = browser.find_element_by_id('robotsRule')
    option2_1 = option2.get_attribute("required")
    option2.click() 
    
    input2 = browser.find_element_by_css_selector("button.btn")
    input2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()