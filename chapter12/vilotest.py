#! python3
# Opens up the newest article on vilo.bydgoszcz.pl and opens it and also opens bydgoszcz.pl in new tab

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

browser = webdriver.Firefox()
browser.get('http://vilo.bydgoszcz.pl/')

read_more_elem = browser.find_element(By.LINK_TEXT, 'Czytaj więcej!')
logging.debug('Find element read_more_elem ok')
read_more_elem.click()

read_bydgoszcz_elem = browser.find_element(By.LINK_TEXT, 'www.bydgoszcz.pl')
logging.debug('Find element read_bydgoszcz_elem ok')
read_bydgoszcz_elem.send_keys(Keys.CONTROL + Keys.ENTER)
