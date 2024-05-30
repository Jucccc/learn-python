
"""
a = int(input("Enter the number: "))
print("The factors are: ", end=' ')
for i in range(1,a+1):
    if a%i == 0:
        if i == a:
            print(i, end = ' ')
        else:
            print(i, end = ', ')

a = int(input("Enter a number: "))
factorial = a
for i in range(a-1,0,-1):
    factorial = factorial * i

print(factorial)

# Generate Fibonacci series

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
n = int(input("Generate Fibonacci Series upto: "))
for i in range(2,n+1):
    a,b=b,a+b
    print(a, end=' ')

# Prime numbers
a = int(input("Enter a number: "))
for i in range(2,a):
    if a%i == 0:
        print(a,'is not a prime number.')
        break
else:
    print(a,'is a prime number')

# print the sum of digits of any number until it becomes a single digit
# I modified this to a recursive call because I think the example was wrong

def getSod(num):
    sod = 0
    while(num>0):
        temp=num%10
        sod=sod+temp
        num=num//10
    return sod

num = int(input("Enter a number: "))
tempNum = num

finalSod = getSod(tempNum)
while len(str(finalSod)) > 1:
    finalSod = getSod(finalSod)

print("The total sum of digits of number is:", finalSod)
"""

# Print a pattern

num = int(input("Enter a number: "))

for i in range(num,0,-1):
    for j in range(i):
        print(i-j,end=' ')
    print()
