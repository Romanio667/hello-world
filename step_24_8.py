from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
button = browser.find_element_by_id('book')
button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
s=calc(int(x))

button1 = browser.find_element_by_id('solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)   

input1 = browser.find_element_by_id('answer')
input1.send_keys(s)
    
button1.click()
//sdsd