import sys
sys.path.append(".")  # Add the current directory to the Python path
#from conftest import driver
import conftest
import pages.home_page
import pages.flights_page
import pages.selectflights_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# test the booking functionality

# forgive me, will encapsulate all of this inside a class soon. No logging and exception handling yet.
# test booking flights
def testbooking():
    pages.home_page.bookflightsbtn()
    pages.flights_page.selectorigin() # enter origin country - hardcoded at the moment will be data driven in the future
    pages.flights_page.selectdestination()  #enter destination country - hardcoded at the moment will be data driven in the future
    pages.flights_page.departdate()  # enter departure date - hardcoded at the moment will be data driven in the future
    pages.flights_page.returndate() # enter return date - hardcoded at the moment will be data driven in the future
    pages.flights_page.selectdatebtn()
    pages.flights_page.searchdatebtn()
    pages.selectflights_page.flightselect()
    pages.selectflights_page.continuebtn()

