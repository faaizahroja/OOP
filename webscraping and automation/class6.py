from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.get("https://www.bbc.com/news")


# give some time to load the page
time.sleep(3)


# Now slow down
current_position = 0
scroll_step = 50


# run an infinite loop to scroll down the page 
while True:
    current_position = current_position + scroll_step   
    
    # now scroll down to the current position 
    driver.execute_script(f"window.scrollTo(0, {current_position})")
    
    
    # give a little time to load the page or to observe the scroll
    time.sleep(0.1)