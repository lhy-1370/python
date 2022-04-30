

def logger(func):
    def wrapper(arg):
        print("함수 시작")
        func(arg)
        print("함수 끝")
    return wrapper


@logger
def print_hello(name):
    print(f"hello {name}")

@logger
def print_bye(name):
    print(f"bye {name}")


print_hello('startcoding')
print_bye('fastcampus')
