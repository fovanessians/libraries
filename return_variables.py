x = 5
y = 7
print('x is: ' ,x)
print('x is: ' ,y)

def tryReturn(x, y):
    a = x + y
    print('a is: ', a)
    b = x * y
    print('b is: ', b)
    return a, b
var1 = tryReturn(x, y)
print('var1 is: ', var1)

print('First element of var1 is: ', var1[0])
print('Second element of var1 is: ', var1[1])
