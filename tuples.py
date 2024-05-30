from collections import namedtuple

# Tuple is an immutable version of list
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

iron_man = ('Tony Stark', 2009)
print('type of iron_man:', type(iron_man))
captain_america = ('Steve Rogers', 2011)
civil_war = iron_man[:1] + captain_america[:1]
print('after tuple concatenation:',civil_war)
print('type after tuple concatenation:',type(civil_war))

dummy_tuple = ('dummy tuple')
print('type of dummy tuple:',type(dummy_tuple))
not_dummy_tuple = ('not a dummy tuple',)
print('type of a not dummy tuple:',type(not_dummy_tuple))
# del(iron_man[0])

'''
Tuple packing and unpacking in Python refers to the process of combining
multiple values into a tuple or extracting values from a tuple, respectively.

Tuple packing is the creation of a tuple by placing multiple values separated
by commas, without explicitly using parentheses. --> tuple = val1,val2,val3

Tuple unpacking is assigning the values of a tuple to multiple variables
in a single line. --> var1,var2,var3 = tuple
'''

avengers = ('Tony','Steve','Natasha','Bruce') # Packing tuples
print('Type of avengers:',type(avengers))

(Iron_Man, Captain_America, Black_Widow, Hulk) = avengers # Unpacking tuple

print(Iron_Man)
print('Type of Iron_Man:',type(Iron_Man))

c = 4,5
print('Type of c:',type(c))
a,b = 4,5
print('a:',a)
print('Type of a:',type(a))

d,e,f,_ = 6,7,8,9
print('underscore:', _)

g,h,*i = 10,11,12,13,14,15
print('g,h,*i:',g,h,i)
print('Type of h:',type(h))
print('Type of *i:',type(i))

*j,k,l = 16,17,18,19,20,21
print('*j,k,l:',j,k,l)

'''
Namedtuples

It's a lightweight class.
'''

Person = namedtuple('Person',['name','age'])
person1 = Person('John',30)

print('person1 name and age:',person1.name,person1.age)
print('access person1 fields by index:',person1[0],person1[1])

# converting lists and tuples

my_list = ['one','two','three']
print('my_list:',my_list)
print('Type of my_list:',type(my_list))
my_list_tpl = tuple(my_list)
print('avengers_tpl:',my_list_tpl)
print('Type of avengers_tpl after converting:',type(my_list_tpl))
my_new_list = list(my_list_tpl)
print('my_new_list:',my_new_list)
print('Type of my_new_list:',type(my_new_list))
