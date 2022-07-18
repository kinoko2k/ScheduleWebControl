import time
from selenium import webdriver
import chromedriver_binary
 
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
 
search = driver.find_element_by_name('q')
search.send_keys('きのこ')
search.submit()
time.sleep(5)
driver.quit()
