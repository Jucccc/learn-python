# Generator generate iterator
# use yield() function to cretate generator

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