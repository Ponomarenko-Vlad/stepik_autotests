from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
try: 
    num1_elem = browser.find_element_by_id('num1')
    num1 = int(num1_elem.text)
    num2_elem = browser.find_element_by_id('num2')
    num2 = int(num2_elem.text)
    answer = Select(browser.find_element_by_tag_name("select"))
    answer.select_by_value(str(num1+num2)) # ищем элемент с текстом "Python")
    button = browser.find_element_by_class_name('btn')
    button.click()
    

finally:
    time.sleep(15)