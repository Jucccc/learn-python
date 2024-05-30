#from __future__ import braces
import this
from platform import python_version
from keyword import kwlist

print("")

print("The python version being used is: ", python_version())
print("")
kwords = kwlist
#print("Number of Python keywords: ", len(kwords))
print("The ",len(kwords), " Python keywords: ", kwords)
print("the tpye of kwlist output: ", type(kwords))

"""
a = '100'
b = 100.1
c = "Python"
d = '''Python'''
print(a,b,c,d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("")
num = int(input("Enter the number: "))
if (rem := num % 2) == 0:
    print(num,'is an even number and the reminder is:', rem)
else:
    print(num,'is an odd number and the reminder is:',rem)

print("")
a, b = 10, 20
_min = a if a < b else b
print('The minimum value is:', _min)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a == b:
    print("The two numbers are equal:",a,b)
elif (a > b):
    print("The greater number is: ", a)
else:
    print("The greater number is: ", b)


# square root with exponent operator **

num = int(input("Enter a number: "))
sq_rt = num ** 0.5
print("The square root of",num,"is",sq_rt)
print("Raising the number",num,"to the power of 2 is",num ** 2)
numtwo = int(input("Enter another integer number: "))
print("Raising 2 to the power of",num,"is",2 ** numtwo)

"""

# swap values between variables using Python's Tuple Packing and Unpacking

a,b = 5,6
print(a,b)
a,b = b,a
print(a,b)

# match case 

rich_avenger = 'Tony'

match rich_avenger:
    case 'Tony' | 'IronMan':
        print(rich_avenger,'is the richest avenger')
    case _:
        print(rich_avenger,'is not the richest avenger')
