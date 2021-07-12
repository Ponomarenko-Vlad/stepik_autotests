from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = ('http://suninjuly.github.io/get_attribute.html')

try:    
    browser = webdriver.Chrome()
    browser.get(link)

    sure = browser.find_element_by_id('treasure')
    x = sure.get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    check = browser.find_element_by_id('robotCheckbox')
    check.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
