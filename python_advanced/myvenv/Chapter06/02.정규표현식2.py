import re

str1 = '010-2343-3333'
result1 = re.match('\d{2,3}-\d{3,4}-(\d{4})$', str1)
print(result1.group(1))

str2 = '010-2343-7888,010-2343-1234,010-2343-5678,010-2343-9999,010-2343-2222'
result2 = re.finditer('\d{2,3}-\d{3,4}-(\d{4})(?=,|$)', str2)

for idx, result in enumerate(result2, 1):
    print(f'{idx} {result.group(1)}')


str3 = '010-2343-3333'
result3 = re.sub('(?<=\d{3}-\d{4}-)\d{4}', '****', str3)
print(result3)


datas = [
    '2022/08/08',
'1000/01/01',
'9999/12/31',
'900/02/02',
'12000/10/26',
'2021/13/01',
'2023/2/02',
'2024/06/3',
'2023/06/35'
]

regex = '^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-2]|3[01])$'

for data in datas:
    matchObj = re.match(regex, data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f'{data} {result}')


datas2 = [
'startcoding@maver.com',
'start-coding@maver.com',
'start_coding@maver.co.kr',
'startcoding@k-mail.com',
'@maver.com',
'startcoding?@k-mail.com',
'startcoding@k-mail',
'startcoding@maver'
]

regex = re.compile('^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-\.]+$')

for data in datas2:
    matchObj = regex.match(data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f'{data} {result}')