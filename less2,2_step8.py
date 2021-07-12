from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Kykan")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Vanya@mail.ru")
    upload = browser.find_element_by_id("file")
    #upload.click()
    current = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current, 'test.txt')
    upload.send_keys(file_path)
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)