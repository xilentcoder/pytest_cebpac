import sys
sys.path.append(".")  # Add the current directory to the Python path
#from conftest import driver
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testtitle():
    WebDriverWait(conftest.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
    print(conftest.driver.title)


