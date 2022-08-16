from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

br = webdriver.Chrome('/usr/bin/chromedriver')

#br.execute_script("window.open('about:blank', 'firsttab');")
br.get("https://nekoumoku.com/")
sleep(4)
br.find_element(By.ID,"wpdlc-button-icon").click()
mssge = br.find_element(By.ID, "wpdlc-widget-app-chats-send-message-textarea")

while( True ): 
    mssge.send_keys(get_random_string(110))
    #sleep(1)
    br.find_element(By.ID,"wpdlc-chats_sendMessage").click()