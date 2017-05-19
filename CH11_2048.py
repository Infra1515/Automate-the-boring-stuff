#! python 3
# 2048
#
# 2048 is a simple game where you combine tiles by sliding them up, down, left, or
# right with the arrow keys. You can actually get a fairly high score by repeatedly
#  sliding in an up, right, down, and left pattern over and over again. Write a
#  program that will open the game at https://gabrielecirulli.github.io/2048/
#  and keep sending up, right, down, and left keystrokes to automatically play the game


from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
click_elem = browser.find_element_by_class_name('container')


while True:
    click_elem.send_keys(Keys.UP)
    click_elem.send_keys(Keys.RIGHT)
    click_elem.send_keys(Keys.DOWN)
    click_elem.send_keys(Keys.LEFT)
