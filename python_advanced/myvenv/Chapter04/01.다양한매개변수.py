def my_func(a,b):
    print(a,b)

my_func(2,3)


def post_info(title,content='내용없음'):
    print(title, content)

post_info("출석", "안출석")
post_info("출석")

def post_info2(content='내용없음',title='제목없음'):
    print(title, content)

post_info2("출석", "안출석")
post_info2("출석")
post_info2()


# 람다 함수
print((lambda a : a - 1)(90))

print((lambda a : True if a > 0 else False)(2))

is_positive_number = lambda a : True if a > 0 else False
print(is_positive_number(-2))



# map 함수
m = list(map(int, ['1', '2', '3']))
print(m)



items = ['  로지텍마우스  ', '   로지텍키보드   ']
for i in range(len(items)):
    items[i] = items[i].strip()

print(items)



items = ['  로지텍마우스  ', '   로지텍키보드   ']
def strip_all(x):
    return x.strip()
items = list(map(strip_all, items))
print(items)

items = ['  로지텍마우스  ', '   로지텍키보드   ']
items = list(map(lambda x : x.strip(), items))
print(items)


def func(x):
    return x < 0
print(list(filter(func, [-3, -2, 0, 5, 7])))



