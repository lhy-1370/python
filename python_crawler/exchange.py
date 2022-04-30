import requests as req

res = req.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

html = res.text

pos = html.find('미국 USD')
print(pos)

s = html.split('<span class="value">')[1].split('</span>')[0]
print(s)