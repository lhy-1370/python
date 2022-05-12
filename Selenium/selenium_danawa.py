from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os


options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
#options.add_argument("headless")


chrome = webdriver.Chrome(r"C:\Users\LHY\Documents\python\Selenium\chromedriver", options=options)
wait = WebDriverWait(chrome, 10)

def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def finds_present(css):
    find_present(css)
    return chrome.find_elements_by_css_selector(css)

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements_by_css_selector(css)

def leftFrame():
    find_visible("iframe#ifrmProduct")
    chrome.switch_to.frame("ifrmProduct")

def rightFrame():
    find_visible("iframe#ifrmWish")
    chrome.switch_to.frame("ifrmWish")

def choose_one(text, options):
    print("---------")
    print(text)
    print("---------")

    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    choose = input("-> ")
    return int(choose) - 1

category = {
    "cpu": "873",
    "메인보드": "875",
    "메모리": "874",
    "그래픽카드": "876",
    "ssd": "32617",
    "케이스": "879",
    "파워": "880",
}

category_css = {
    c: "dd.category_" + category[c] + " a" for c in category
}

chrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti")

# rightFrame()
find_visible(category_css["cpu"]).click()
time.sleep(1)

# leftFrame()
options = finds_visible("input[name=makerCode] + span")

i = choose_one("cpu 제조사를 골라주세요", [x.text for x in options])
options[i].click()

title = ""
cpuno = ""
if i == 0:
    title = "인텔 CPU종류"
    cpuno = "873|40"
elif i == 1:
    title = "AMD CPU종류"
    cpuno = "873|312287"

options = finds_visible(f"div.search_cate_title")
# for i in range(len(options)):
#     print(f"{i+1}. {options[i].text}")
for i in range(len(options)):
    if options[i].text == title:
        # print(f"yes {i+1}. {options[i].text}")
        options[i].find_element_by_xpath('..').find_element_by_css_selector("div button").click()
        break
    else:
        # print(f"no {i+1}. {options[i].text}")
        continue

options = finds_visible(f"input[value*='{cpuno}'] + span")
# for i in range(len(options)):
#     print(f"{i+1}. {options[i].text}")
i = choose_one("cpu 종류를 골라주세요", [x.text for x in options])
options[i].click()

time.sleep(6)

chrome.quit()