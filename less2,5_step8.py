from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = browser.find_element_by_id('price')
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element_by_id('book')
    button.click()
    sure = browser.find_element_by_id('input_value')
    x = sure.text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button1 = browser.find_element_by_id('solve')
    #browser.execute_script("returt arguments[0].scrollIntoView(true);", button1)
    #WebDriverWait(browser, 5).until(EC.presence_of_element_located(By.ID, "solve"))

    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    # browser.quit()