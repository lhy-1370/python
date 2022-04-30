def func(x, y):
    return x + y

add = func
print(add(3,4))



def mul(x, y):
    return x * y

def div(x, y):
    return x / y

calculator = [mul, div]
print(calculator[0](5,6))




def inputData():
    data = input("데이터 입력>>>")
    return data

def start(func):
    print("입력한 데이터는", func())

start(inputData)




def plusTen(a):
    return a + 10

def func(x):
    return plusTen(x)

print(func(5))

