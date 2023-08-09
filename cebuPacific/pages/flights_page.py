import sys
sys.path.append(".")  # Add the current directory to the Python path
#from conftest import driver
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# forgive me, will encapsulate all of this inside a class soon. No logging and exception handling yet.
def selectorigin(): # select origin australia, melbourne
    WebDriverWait(conftest.driver, 20).until(EC.presence_of_element_located((By.ID, "originFormControl-0")))
    conftest.driver.find_element(By.ID, "originFormControl-0").click()
    time.sleep(5)
    conftest.driver.find_element(By.LINK_TEXT, "Australia").click()
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".is-active .ng-tns-c19-16:nth-child(1) > .ng-tns-c19-16 > .ng-tns-c19-16").click()


#select destination singapore, singapore
def selectdestination():
    destination = "//input[@id=\"\'destinationFormControl-0\"]"
    WebDriverWait(conftest.driver, 20).until(EC.presence_of_element_located((By.XPATH, destination)))
    conftest.driver.find_element(By.ID, "\'destinationFormControl-0").click()
    conftest.driver.find_element(By.LINK_TEXT, "Singapore").click()
    conftest.driver.find_element(By.CSS_SELECTOR, ".is-active > .ng-tns-c19-16 > .ng-tns-c19-16 > .ng-tns-c19-16 > .ng-tns-c19-16").click()

#select departure date
def departdate():
    conftest.driver.find_element(By.CSS_SELECTOR, ".o-form_input:nth-child(1) > .ng-tns-c20-17").click()
    conftest.driver.find_element(By.CSS_SELECTOR, ".c-calendar-month:nth-child(1) > .c-calendar-month-pick").click()
    conftest.driver.find_element(By.CSS_SELECTOR, ".c-calendar-month:nth-child(1) > .c-calendar-month-pick").click()
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".c-calendar-month:nth-child(1) > .c-calendar-month-pick > .ng-tns-c20-17:nth-child(2)").click()
    time.sleep(5)

#select return date
def returndate():
    conftest.driver.find_element(By.CSS_SELECTOR, ".month:nth-child(5) > .ng-tns-c20-17").click()
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".c-calendar-month:nth-child(1) > .c-calendar-month__row:nth-child(3) > .c-calendar-month__cell:nth-child(6) > .c-calendar-month__cell-date > .ng-tns-c20-17").click()
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".c-calendar-month__row:nth-child(3) > .c-calendar-month__cell:nth-child(4) > .c-calendar-month__cell-date > .ng-tns-c20-17").click()


def selectdatebtn():
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".o-btn--primary-blue:nth-child(2)").click()

def searchdatebtn():
    time.sleep(5)
    conftest.driver.find_element(By.CSS_SELECTOR, ".fixed-size").click()

