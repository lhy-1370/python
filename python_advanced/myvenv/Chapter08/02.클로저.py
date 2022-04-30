def outer(name):
    def inner():
        print(name, "님 안녕하세요!")
    return inner

func = outer("startcoding")
func()


def greeting(name, age, gender):
    def inner():
        print(name, "님 안녕하세요!")
        print(age, "나이")
        print(gender, "성별")
    return inner

closure = greeting('나미', 27, 'female')
closure()

print(dir(closure.__closure__))
print(closure.__closure__[0].cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)
