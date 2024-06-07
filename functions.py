def sq(n):
    return n * n

# give function as an input param:
def my_map_func(my_func, list_of_arg):
    result = []
    for i in list_of_arg:
        result.append(my_func(i))
    return result

squares = my_map_func(sq, [4,3,2,1])
print(squares)

# return function as a result
def log_in(msg):
    def login_msg():
        print('Login:',msg)
    return login_msg

user_login = log_in('Welcome')
user_login()

# Find LCM - least common multiple
def find_lcm_my_version(a,b):
    small,big = (a,b) if a < b else (b,a)
    lcm = 0
    biggest = 0
    while lcm == 0:
        biggest = biggest + big
        if biggest % small == 0:
            lcm = biggest
    return lcm

def find_lcm_book_version(a,b):
    if a > b:
        a,b = b,a
    for i in range(b,(a*b)+1,b):
        if i%a==0:
            return i
        
# Euclidean method - [LCM(a,b)=(a*b)/HCF(a,b)]
def hcf(a,b): # Highest Common Factor, or GCD - Greatest Common Divisor
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
    
def lcm(a,b):
    lcm = (a*b)//hcf(a,b)
    return lcm

'''
num_1 = int(input('Give the first number:'))
num_2 = int(input('Give the second number:'))
#print(find_lcm_book_version(num_1,num_2))
print('The LCM is:',lcm(num_1,num_2))
print('The HCF is:',hcf(num_1,num_2))
'''

# Function that do nothing
def abc():
    pass
print(abc())

# Variable number of arguments
def n_values(*a):
    return a
print(n_values(1,2,3))
print(type(n_values()))

def c_to_f(*,degree_celsius):
    return 32 + degree_celsius * 9/5

#c_to_f(98) # not working as it takes only with keyword
print(c_to_f(degree_celsius=98))

def n_values(**b):
    return b
print(n_values(x=1,Y=2,z=3))
print(type(n_values()))

def n_values_2(*a, **b): # usually written as "args, kwargs" - like arguments and keyword arguments
    return a,b
print(n_values_2(1,2,3, x=1,Y=2,z=3))
print(type(n_values_2()))

def avengers_detail(**kwargs):
    if 'real_name' in kwargs:
        print("Real Name:", kwargs['real_name'])
    if 'reel_name' in kwargs:
        print("Reel name:",kwargs['reel_name'])
    if 'super_hero_name' in kwargs:
        print("Super hero name:", kwargs['super_hero_name'])

details = {
    'real_name': 'Robert Downey Jr.',
    'reel_name': 'Tony Stark',
    'super_hero_name': 'Iron Man'
}

# Auto unpack dictionary to function arguments with **
avengers_detail(**details)