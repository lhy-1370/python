from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

from yaml import parse

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
options.headless=True

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

def choose_product(text, products):
    print("---------")
    print(text)
    print("---------")

    for i in range(len(products)):
        name = products[i].find_element_by_css_selector("p.subject a").text
        try:
            price = products[i].find_element_by_css_selector("span.prod_price").text
        except:
            continue
        print(f"{i+1}. {name} {price}")
    choose = input("-> ")
    return int(choose) - 1

def btn_more():
    find_visible("button.search_option_all").click()
    btns_more = finds_visible("div.search_cate_contents button.btn_item_more")
    for btn in btns_more:
        btn.click()

def choose_category(text):
    # 카테고리 클릭
    find_visible(category_css[f"{text}"]).click()
    time.sleep(2)

    # 더보기 누르기
    btn_more()

    # 제조사 불러오기 
    options = finds_visible("input[name=makerCode] + span")
    i = choose_one(f"{text} 제조사를 골라주세요", [x.text for x in options])
    options[i].click()
    time.sleep(2)

    return i

def get_options(text, choosetext, no):
    if text == "메인보드":
        find_visible(f"input[value*='{no}'] + span").click()
    elif text == "그래픽카드":
        find_visible(f"input[value*='{no}'] + span").click()
    else:
        options = finds_visible(f"input[value*='{no}'] + span")
        i = choose_one(f"{choosetext}를 골라주세요", [x.text for x in options])
        options[i].click()

    time.sleep(2)

def get_product():
    # 제품 목록 선택하기
    products = finds_visible("div.scroll_box tr[class^=productList_]")
    i = choose_product("제품을 골라주세요", products)
    products[i].find_element_by_css_selector("a.btn_choice2").click()
    return (products[i].find_element_by_css_selector("p.subject a").text, products[i].find_element_by_css_selector("span.prod_price").text)

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


title = ""
cpuno = ""
mainboardno = ""
graphicno = ""

i = choose_category("cpu")
if i == 0:
    title = "인텔 CPU종류"
    cpuno = "40"
    mainboardno = "2153"
    graphicno = "3518"
elif i == 1:
    title = "AMD CPU종류"
    cpuno = "312287"
    mainboardno = "2154"
    graphicno = "3517"

get_options("cpu", title, "873|" + cpuno)
cpus = get_product()
time.sleep(2)

# 메인보드 선택
choose_category("메인보드")
get_options("메인보드", "제품 분류", "875|499|" + mainboardno)
mainboards = get_product()
time.sleep(2)

# 메모리 선택
choose_category("메모리")
get_options("메모리", "사용 장치", "874|278")
memories = get_product()
time.sleep(2)

# 그래픽카드 선택
choose_category("그래픽카드")
get_options("그래픽카드", "칩셋 제조사", "876|654|" + graphicno)
graphics = get_product()
time.sleep(2)

# ssd 선택
choose_category("ssd")
get_options("ssd", "제품 분류", "32617|14689")
get_options("ssd", "디스크 용량", "32617|14691")
ssds = get_product()
time.sleep(2)

# 케이스 선택
choose_category("케이스")
get_options("케이스", "제품 분류", "879|973")
cases = get_product()
time.sleep(2)

# 파워 선택
choose_category("파워")
get_options("파워", "제품 분류", "880|1086")
get_options("파워", "정격출력", "880|1088")
get_options("파워", "80PLUS인증", "880|13033")
powers = get_product()

print("cpu : " + cpus[0] + ", " + cpus[1])
print("mainboards : " + mainboards[0] + ", " + mainboards[1])
print("memories : " + memories[0] + ", " + memories[1])
print("graphics : " + graphics[0] + ", " + graphics[1])
print("ssds : " + ssds[0] + ", " + ssds[1])
print("cases : " + cases[0] + ", " + cases[1])
print("powers : " + powers[0] + ", " + powers[1])
totalprice = int(cpus[1].replace(',','')) + int(mainboards[1].replace(',','')) + int(memories[1].replace(',','')) + int(graphics[1].replace(',','')) + int(ssds[1].replace(',','')) + int(cases[1].replace(',','')) + int(powers[1].replace(',',''))
print("total price :", totalprice)

time.sleep(10)

chrome.quit()