from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name('btn')
    button.click()
    window = browser.window_handles[1]
    browser.switch_to.window(window)
    sure = browser.find_element_by_id('input_value')
    x = sure.text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button1 = browser.find_element_by_class_name('btn')
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)