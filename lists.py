# Lists are created using square brackets:

rainbow = ["violet",'indigo','blue','green','yellow','orange','red']
print('rainbow:',rainbow)
rainbow = rainbow[::-1]
print('reversed rainbow:',rainbow)

print()

numbers = [1,2,10,3,8,4,9,7,11,5,6]
strNumbers = ['1','5','10','3','8','2','7','4','6','9']
letters = ['c','b','a','d','h','i','q','W','f']

'''
print(numbers)
print(strNumbers)
print(letters)

print('min numbers:',min(numbers))
print('max strNumbers:',max(strNumbers))
print('sum numbers:',sum(numbers))
numbers = sorted(numbers)
print('sorted numbers:',numbers)
print('sorted letters:',sorted(letters))
print('sorted rainbow:',sorted(rainbow))
print('numbers:',numbers)
numbers.reverse()
print('reverse numbers:',numbers)
print('list Juci:',list('Juci'))
print('any:',any([-3,"b",-4]))
print('all:',all([-3,"b",-4]))
print('any empty list:',any([]))
numbers.append(12)
print('after numbers append:',numbers)
numbers.extend(letters)
numbers.append(12)
print('after extend and append 12 numbers:',numbers)
print('count of 12:',numbers.count(12))
numbers.remove(12)  #Removes first occurance only
print('after remove 12:',numbers)
numbers.pop()
print('after pop numbers:',numbers)
numbers.clear()
print('after clear numbers:',numbers)
print('len of numbers:',len(numbers))
print('rainbow:',rainbow)
print('incex of orange:',rainbow.index('orange'))
print('black in rainbow?','black' in rainbow)

# Enumerators

for x,y in enumerate(rainbow,1):
    print(x,y)

print('Index of the first element:',rainbow.index('red'))

# Copy of the list

#rainbowTwo = rainbow  # Shallow copy, new object, but contents points to the same
#rainbowTwo = rainbow.copy()  # Deep copy
#rainbowTwo = rainbow[:]  # Deep copy
rainbowTwo = list(rainbow)  # Deep copy
rainbowTwo.pop()
print('rainbow:',rainbow)
print('rainbowTwo:',rainbowTwo)

# List comprehension

square_list = []
for i in range(10):
    square_list.append(i*i)
print(square_list)

square_list_lc = [j*j for j in range(10)]
print(square_list_lc)

my_data = "Hello Sir. I am 65 years old, and, \
        my height is 5 foot 10 inches and, \
        my biceps are 18 inches wide."
my_list = [int(num) for num in my_data.split() if num.isdigit()]
print(my_list)

data = [0,5,4,3,2,1,0]
print([i for i in data if i != 0])


print('Enter the marks of the subjects:')

avg = sum(marks := [int(i) for i in input().split(' ')])/len(marks)
total_subjects = len(marks)
print('Total number of subjects:',total_subjects)

if avg > 90 and avg <= 100:
    print('Your average score is:',avg,'and your grade is A+')
elif avg > 80 and avg <= 90:
    print('Your average score is:',avg,'and your grade is A')
else:
    print('Your average score is:',avg)
'''

avengers = ['I','am','IronMan']
print(avengers)
my_str = ' '.join(avengers)
print(my_str)

my_list = [4,3,2,1,[9,8,7,6,5]]
print(my_list[:])
print(my_list[4])
print(my_list[4][2])