#! python3
# automatically play the game 2048
# by repeatedly sliding in an up, right, down, and left pattern over and over again

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
time.sleep(4)
cookies_elem = browser.find_element(By.ID, 'ez-accept-all')
cookies_elem.click()

html_elem = browser.find_element(By.TAG_NAME, 'html')
try_again_elem = browser.find_element(By.CLASS_NAME, 'retry-button')
while True:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)
    try:
        try_again_elem.click()
        continue
    except:
        continue

