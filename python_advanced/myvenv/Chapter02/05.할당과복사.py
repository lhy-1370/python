

x = [1,2,3,4,5]
y = x 
y[2] = 0
print(x)
print(y)

print(id(x))
print(id(y))



a = [1,2,3,4,5]
b = a.copy() 
b[2] = 0
print(a)
print(b)

print(id(a))
print(id(b))

