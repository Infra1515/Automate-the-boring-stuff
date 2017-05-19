#! Python 3
# CMD_TERMINAL_EMAILER.py

import sys
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) < 3:
    print('This program is a command line emailer.')
    print('Enter the email adress and then your message')
    exit()
else:
    None

email_adress = sys.argv[1]
email_message = ' '.join(sys.argv[2:])

# selenium part
# login, search for the email and text field, paste, send
browser = webdriver.Firefox()
browser.get('https://mg.mail.yahoo.com/d/compose/')

username_elem = browser.find_element_by_id('login-username')
username_elem.send_keys('infra1515')

next_elem = browser.find_element_by_id('login-signin')
next_elem.click()
# The program needs to wait, because the page loads slowly
# See more here http://stackoverflow.com/questions/39320283/
# selenium-common-exceptions-elementnotvisibleexception-message-element-is-not-c
wait = WebDriverWait(browser, 10)
pass_ = wait.until(EC.visibility_of_element_located((By.ID, "login-passwd")))
pass_.clear()
pass_.send_keys('INSERTPASSWORDHERE')
next_elem = browser.find_element_by_id('login-signin')
next_elem.click()
# mail_element_wait = wait.until(EC.visibility_of_element_located((By.CLASS, 'uh-mail-link')))
# mail_element_wait.clear()
# # browser.find_element_by_link_text('Mail')
# mail_element.click()



# First part is done - Selenium logs is. Now I need to click compoose,  paste sys.argv[1],[2]
# to email adress and text field and click send.
# How to paste ? Pyperclicp + send.buttons(CTRL-V)

pyperclip.copy(sys.argv[1])
adress_field = wait.until(EC.element_to_be_clickable((By.ID, "message-to-field")))
adress_field.click()
adress_field.send_keys(Keys.CONTROL + "v")
pyperclip.copy(sys.argv[2])
subject_field = wait.until(EC.element_to_be_clickable((By.ID, 'editor-container')))
subject_field.click()
subject_field.send_keys(Keys.CONTROL + 'v')
send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'q_Z2aVTcY e_dRA k_w r_P H_6VdP s_3mS2U en_0 M_1gLo4F V_M cZ1RN91d_n y_1ACvVU A_6EqO u_e69 b_0 C_52qC I4_Z29WjXl ir3_2d4VCo it3_dRA')))
send_button.click()
