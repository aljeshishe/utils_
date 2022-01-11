from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

print('selenium')

def wait_element(driver, xpath, timeout=10):
    element = EC.presence_of_element_located((By.XPATH, xpath))
    return WebDriverWait(driver, timeout=timeout).until(element)

