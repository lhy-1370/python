from selenium import webdriver
import time

browser = webdriver.Chrome("./Selenium/chromedriver")
browser.get("https://web.lotteibank.com/lotteatm.jsp")
time.sleep(10)
browser.close()


# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
# browser.get("http://naver.com")
# print(browser.title)
# browser.close()
