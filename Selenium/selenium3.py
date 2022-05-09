from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
#options.add_argument("headless")


chrome = webdriver.Chrome(r"C:\Users\LHY\Documents\python\Selenium\chromedriver", options=options)
chrome.get("https://shopping.naver.com")
#time.sleep(3)
#el = chrome.find_element_by_css_selector("input[name=query")
wait = WebDriverWait(chrome, 10)
#el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query")))
#print(el)
def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[name=query]")
search.send_keys("아이폰 케이스\n")
time.sleep(3)

#button = find(wait, "a.co_srh_btn")
#button.click()
#time.sleep(3)

chrome.close()