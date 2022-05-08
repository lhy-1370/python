from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
#options.add_argument("no-sandbox")
#options.add_argument("headless")
chrome = webdriver.Chrome(r"C:\Users\LHY\Documents\python\Selenium\chromedriver", options=options)
#edge = webdriver.Edge()
#ie = webdriver.Ie()
chrome.get("https://naver.com")
chrome.get("https://shopping.naver.com")
chrome.back()
chrome.forward()
time.sleep(3)
chrome.close()