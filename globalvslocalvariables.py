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

#c = min([1,2,3,4]) #  - not working because we override the function
c = min()
print(c)