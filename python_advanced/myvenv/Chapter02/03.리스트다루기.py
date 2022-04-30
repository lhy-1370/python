fruits = ['apple', 'orange', 'mango']
del fruits[1]
print(fruits)

numbers = [5, 1, 2, 8, 3]
numbers.sort()
print(numbers)

titles = ['출석!!', '출석인증합니다!', '출석이요!!']

for index, title in enumerate(titles, 1):
    print(f'{index} 번째 글입니다. 제목 : {title}')