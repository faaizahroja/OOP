# Topic: Login Automation
from selenium import webdriver
from selenium.webdriver.common.by  import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions   as EC
import time



driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/login")


usernameInput = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)

usernameInput.send_keys("mehedi")

time.sleep(3)