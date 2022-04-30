import pay_module

print(pay_module.version)

pay_module.printAuthor()

pay_info = pay_module.Pay("A102030", 13000, "2021-06-13")
print(pay_info.get_pay_info())

print(pay_module.__name__)