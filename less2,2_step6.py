from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
try: 
    x_elem = browser.find_element_by_id('input_value')
    x = int(x_elem.text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button = browser.find_element_by_class_name('btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    check = browser.find_element_by_id('robotCheckbox')
    check.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button.click()
    

finally:
    time.sleep(15)