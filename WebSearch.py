import schedule
from time import sleep
from selenium import webdriver
import chromedriver_binary

def task():
    driver = webdriver.Chrome()
# 指定サイトで実行
    driver.get('https://www.google.com/')
# 検索tagがq
    search = driver.find_element_by_name('q')
# 検索ワード
    search.send_keys('リンゴ')
    search.submit()
    driver.quit()
    print("Task running now")

schedule.every(1800).seconds.do(task)

while True:
    schedule.run_pending()
    sleep(1)
