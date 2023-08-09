import sys
sys.path.append(".")  # Add the current directory to the Python path
#from conftest import driver
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# forgive me, will encapsulate all of this inside a class soon.
def flightselect(): # select flights
    time.sleep(5)
    conftest.driver.execute_script("window.scrollTo(0,0)")
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c33-48:nth-child(1) > .flight-time:nth-child(2) > .time").click()
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c34-50 > .promo:nth-child(1) > .o-btn").click()
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c33-56:nth-child(1) > .flight-time:nth-child(2) > .time").click()
    time.sleep(7)
    conftest.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c34-57 > .promo:nth-child(1) > .o-btn").click()
    time.sleep(5)

def continuebtn():
    conftest.driver.find_element(By.LINK_TEXT, "Continue").click()