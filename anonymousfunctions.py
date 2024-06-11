# also called lambda functions
# works in conjunction with filter(), map() and reduce()
# filter() - filter the elements
# map() - map a function to each element
# reduce() - reduce to a single value

from functools import reduce

# multiply with 2:
def sq(n):
    return n*2
print(sq(3))

m = lambda n:n*2
print(m(3))

# find max:
mx = lambda m,n:m if m>n else n
print(mx(5,7))

# return a list which contains a squared value of each number in the input list
def sq_list(lst):
    lst2 = []
    for x in lst:
        lst2.append(x**2)
    return lst2
a = [4,3,2,1]
print(sq_list(a))

lst = [4,3,2,1]
print(list(map(lambda x:x**2,lst)))

# keep the numbers which greater than 2
lst_2 = [4,3,2,1]
print(list(filter(lambda x:x>2, lst_2)))

# do the numbers greater than 2?
print(list(map(lambda x:x>2, lst_2)))

# multiply each value of the list and print the result - reduce
def prod_terms(a):
    mul = a[0]
    for i in range(1, len(a)):
        mul *= a[i]
    return mul
a = [1,2,3,4]
print(prod_terms(a))

a = [1,2,3,4]
print(reduce(lambda x,y:x*y,a))