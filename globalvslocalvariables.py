# priority rule: LEGB - local, enclosing scope, global, built-in
# there is a global keyword
import builtins

m = 1
def sq(n):
    global m
    m = n ** 2
    return m
print(sq(5))
print(m)

a = 10
def global_check():
    a = 20
    b = globals()['a']
    print('variable inside function:',a)
    globals()['a'] = 50

global_check()
print('variable outside function:',a)

# override the builtin min() function
def min():
    pass

#c = min([1,2,3,4]) #  - not working because we override the built-in function
c = min()
print(c)

def outer():
    x = 'outer of x'
    def inner():
        x = 'inner of x' # enclosing scope
        print(x)
    inner()
    print(x)

outer()

def outer2():
    y = 'outer of y'
    def inner():
        nonlocal y # overwrite scope
        y = 'inner of y'
        print(y)
    inner()
    print(y)

outer2()

# Closure functions - inner function variable can access the outer function variables
def add_to_fun(val1):
    def add_fun(val2):
        return val1 + val2
    return add_fun

add_fun2 = add_to_fun(3)
print(add_fun2(4))
print(add_to_fun(3))