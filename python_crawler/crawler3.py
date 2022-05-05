from bs4 import BeautifulSoup as BS
import requests as req

url = "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0%20%EC%BC%80%EC%9D%B4%EC%8A%A4&frm=NVSHATC&prevQuery=%EC%95%84%EC%9D%B4%ED%8F%B0%EC%BC%80%EC%9D%B4%EC%8A%A4"
res = req.get(url)
soup = BS(res.text, "html.parser")

# ul class list_basis
# div 아래 첫번째 자식 a
# title
arr = soup.select("ul.list_basis div>a:first-child[title]")
for a in arr:
    print(a.get_text(strip=True))