import re

str = 'love people around you, love your work, love yourself'

result = re.match('love', str)
print(result)

result = re.search('people', str)
print(result)

result = re.findall('love', str)
print(result)


results = re.finditer('love', str)
print(results)

for result in results:
    print(result)

str2 = 'Hey Guys, read books'

result = re.fullmatch('.*', str2)
print(result)

#result = re.search('people', str)
print(result.group())
print(result.start())
print(result.end())
print(result.span())



