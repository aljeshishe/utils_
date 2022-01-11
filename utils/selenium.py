import utils


VERSIONS = {'selenium': '==4.1.0'}
print('selenium')

def wait_element(driver, xpath, timeout=10):
    selenium_ = utils.imp.install_import('selenium', VERSIONS['selenium'])
    WebDriverWait = selenium_.webdriver.support.ui.WebDriverWait
    presence_of_element_located = selenium_.webdriver.support.expected_conditions.presence_of_element_located
    By = selenium_.webdriver.common.by.By

    element = presence_of_element_located((By.XPATH, xpath))
    return WebDriverWait(driver, timeout=timeout).until(element)
