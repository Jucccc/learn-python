# Generator generate iterator
# use yield() function to cretate generator
# Advantages: save huge heaps of memory at the cost of having
# extra execution time for generating the next iterable object

def sq_num(my_list):
    result = []
    for i in my_list:
        yield (i*i)

a = sq_num([4,3,2,1])
print(a)
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
for x in a:
    print(x, end=' ')

# Generator comprehension

b = [4,3,2,1]
gen_com = (x*x for x in a)
for i in gen_com:
    print(i, end=' ')

# Fibonacci series
def fib_series(a):
    x, y = 0, 1
    while True:
        z = x + y
        if z < a:
            yield z
            x, y = y, z
        else:
            break
gen_fib = fib_series(10)
print(gen_fib)
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))