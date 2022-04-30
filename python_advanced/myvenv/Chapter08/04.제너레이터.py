def season_generator(*args):
    for arg in args:
        yield arg

g = season_generator('spring', 'summer', 'autumn', 'winter')

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


def func():
    print("첫번째 작업 중...")
    yield 1

    print("두번째 작업 중...")
    yield 2

    print("세번째 작업 중...")
    yield 3

ge = func()
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)



double_generator = (i * 2 for i in range(1,10))
print(double_generator)
for i in double_generator:
    print(i)



## 리스트는 모든 값을 저장
## 제너레이터는 표현식만 저장하고 __next__를 사용할때 값을 만들어서 사용
import sys

list_data = [i * 3 for i in range(1, 10000 + 1)]
generator_data = (i * 3 for i in range(1, 10000 + 1))

print(sys.getsizeof(list_data))
print(sys.getsizeof(generator_data))


