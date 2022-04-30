name = '기준'
duration = 7

message = name + '님 수강기간이 ' + str(duration) + '일 남았습니다.'
print(message)

message_format = f'{name}님 수강기간이 {duration}일 남았습니다.'
print(message_format)



a = 'Hello {2} {1} {0} {2}'.format('apple', 'pineapple', 'pen')
print(a)

b = 'Hello {} {} {}'.format('apple', 'pineapple', 'pen')
print(b)

name1 = 'apple'
name2 = 'pineapple'
name3 = 'pen'

c = f'Hello {name1} {name2} {name3}'
print(c)
