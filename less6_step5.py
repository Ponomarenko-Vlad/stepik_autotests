from selenium import webdriver
import math
import time

try:
    link = 'http://suninjuly.github.io/find_link_text'
    driver = webdriver.Chrome()
    driver.get(link)    
    link1 = driver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link1.click()

    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(20)
    driver.quit()
