from selenium import webdriver
from selenium.webdriver.common.by import By
import sys, time

#acquire basic data
recipient = sys.argv[1]
title = sys.argv[2]
text =' '.join(sys.argv[3:])

#open the browser and login
browser = webdriver.Firefox()
browser.get('https://konto.onet.pl/en/signin')
time.sleep(5)

cookies_accept = browser.find_element(By.CSS_SELECTOR, 'button.cmp-button_button:nth-child(2)')
cookies_accept.click()

email_login_elem = browser.find_element(By.ID, 'email')
email_login_elem.send_keys('bartas1999@onet.pl')
email_login_elem.submit()
time.sleep(5)

password_login_elem = browser.find_element(By.NAME, 'password')
password_login_elem.send_keys('ten@99O270')
password_login_elem.submit()

onet_mail = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div[2]/ul/li[1]/a')
onet_mail.click()

new_message = browser.find(By.CLASS_NAME, 'Styles__Label-sc-1dtturh-0 dpjsSr')
new_message.click()

#write and send email
recipient_elem = browser.find_element(By.CLASS_NAME, 'styles__BubbleField-n6c5mc-0 eFFjCJ')
recipient_elem.send_keys(recipient)

title_elem = browser.find_element(By.CLASS_NAME, 'styles__FormInputField-sc-5gxzyf-0 jgJnwp')
title_elem.send_keys(title)

text_elem = browser.find_element(By.ID, 'CONTENT_TEXTAREA_ID')
text_elem.send_keys(text)

send_elem = browser.find_element(By.CLASS_NAME, ':Button__ButtonStyled-xzcupb-0 hCUQCz')
send_elem.click()
