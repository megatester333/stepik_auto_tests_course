from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button1 = browser.find_element(By.ID, "book")
# говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button1.click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.CLASS_NAME, "form-control")
input1.send_keys(y)
button2 = browser.find_element(By.ID, "solve")
button2.click()
time.sleep(10)
browser.quit()
