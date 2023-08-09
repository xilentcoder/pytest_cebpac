import sys
sys.path.append(".")  # Add the current directory to the Python path
#from conftest import driver
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def bookflightsbtn():
    a = ActionChains(conftest.driver)
    WebDriverWait(conftest.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Book')))
    bookhover = conftest.driver.find_element(By.LINK_TEXT, "Book")
    a.move_to_element(bookhover).perform()
    time.sleep(5)
    conftest.driver.find_element(By.LINK_TEXT, "Flights").click()