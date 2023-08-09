import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = None
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

# use webdriver manager for selenium 4
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.fixture(autouse=True)
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.cebupacificair.com/en-PH/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/omnix-project/omnix-main-master-page/div[2]/div/a[1][text()='I agree']").click()  # agree to privacy terms
    yield
    time.sleep(10)
    driver.quit()