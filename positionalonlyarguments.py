# positional only arguments (/ sign)

def raised_to(x,y,/,z = None):
    w = x ** y
    if z is not None:
        w %= z
    return w
#print(raised_to(x = 3, y = 5, z = 6)) # TypeError: raised_to() got some positional-only arguments passed as keyword arguments: 'x, y'
print(raised_to(3, 5, z = 6))
print(raised_to(3, 5, 6))
