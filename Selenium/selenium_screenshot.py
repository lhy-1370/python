from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()
# options.set_headless(True)
# options.add_argument("--headless")
options.headless=True

chrome = webdriver.Chrome("./Selenium/chromedriver", options=options)
wait = WebDriverWait(chrome, 10)

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements_by_css_selector(css)

chrome.get("https://www.naver.com")
find_visible("input#query").send_keys("패스트캠퍼스\n")

e = find_visible("li[data-cr-rank='3']")
chrome.execute_script("""
document.querySelector("li[data-cr-rank='3']").setAttribute('style', 'border:10px solid red')
""")

# e.screenshot("./Selenium/test.png")

# chrome.save_screenshot("./Selenium/test.png")

chrome.set_window_size(1000, 10000)
body = find_visible("body")
body.screenshot("./Selenium/test.png")

chrome.quit()
