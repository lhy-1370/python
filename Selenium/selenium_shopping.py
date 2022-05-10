from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip


options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
#options.add_argument("headless")


chrome = webdriver.Chrome(r"C:\Users\LHY\Documents\python\Selenium\chromedriver", options=options)

wait = WebDriverWait(chrome, 30)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")

#login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

#input_id.send_keys("lhy1370")
pyperclip.copy("lhy1370")
input_id.send_keys(Keys.CONTROL, "v")

#input_pw.send_keys("wngml11!!Wkd")
pyperclip.copy("wngml11!!Wkd")
input_pw.send_keys(Keys.CONTROL, "v")

input_pw.send_keys("\n")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button")))
# a[class="logout_button"]
# a[class^="logout"]
# a[class$="button"]
# a[class*="out_but"]

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys("아이폰 케이스")
time.sleep(1)
search.send_keys("\n")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^=basicList_info_area__]")))

# 스크롤
for i in range(3):
    #chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    chrome.execute_script("window.scrollBy(0, " + str((i+1) * 1000) + ")")
    time.sleep(1)


items = chrome.find_elements_by_css_selector("div[class^=basicList_info_area__]")

for item in items:
    # 광고 빼기
    #try:
    #    item.find_element_by_css_selector("button[class^=ad_")
    #    continue
    #except:
    #    pass
    print(item.find_element_by_css_selector("a[class^=basicList_link__]").text)

#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class^=basicList_link__]"))).click()
chrome.find_elements_by_css_selector("a[class^=basicList_link__]")[9].click()

time.sleep(2)

chrome.switch_to.window(chrome.window_handles[1])
print("\n")
print(chrome.title)


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[aria-haspopup='listbox']")))
c_options = chrome.find_elements_by_css_selector("a[aria-haspopup='listbox']")

# 첫번째 옵션 클릭
c_options[0].click()
time.sleep(0.1)
chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(2) a[role=option]").click()
#chrome.find_elements_by_css_selector("ul[role=listbox] a[role=option]")[3].click()

# 두번째 옵션 클릭
c_options[1].click()
time.sleep(0.1)
chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(1) a[role=option]").click()

# 결제하기 버튼 누르기
chrome.find_element_by_css_selector("div[class*='N=a:pcs.buy'] a").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._doPayButton"))).click()


time.sleep(5)

#chrome.close()
chrome.quit()