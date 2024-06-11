# priority rule: LEGB - local, enclosing scope, global, built-in
# there is a global keyword
import builtins, math

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
print(add_fun2.__name__)
print(add_fun2(4))
print(add_to_fun(3))

def outer_func_print_output():
    message = 'Python for fun'
    def inner_func():
        print(message)
    return inner_func() # calling the inner_func()

outer_func_print_output()

def outer_func_func_output():
    message = 'Python for fun'
    def inner_func():
        print(message)
    return inner_func # do not calling the inner_func() just return it
new_func = outer_func_func_output()
print(new_func.__name__)
new_func() # call here

# if we are not allowed to modify the existing function but we want to add additional functionality
# - decorate the original function:
def check_div_op(div_op_func): # decorator function
    def inner(a,b):
        if b == 0:
            print('Not allowed to divide by zero')
            return
        div_op_func(a,b)
    return inner

@check_div_op # pointer to the decorator function
def div_op(a,b): # original function
    return a/b

''' No need these if we have a pointer on the original function to the decorator function:
div_func = check_div_op(div_op)
print(div_func(5,0))
'''

print(div_op(5,0))

# return multiple values

def circle(rad):
    cir = 2 * math.pi * rad
    area = math.pi * rad * rad
    return(cir,area)
rad = int(input('Enter the radius of the circle: '))
print('The circumference and area are:',circle(rad))