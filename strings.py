# Strings can be written in single, double and triple quotes

iron_man = "I love you '3000'"
print(iron_man)
iron_man = '''"I love you '3000'"'''
print(iron_man)
multiple_lines = '''I
am
Iron Man'''
print(multiple_lines)
multiple_lines_backslash = "I\nam\nIron Man"
print(multiple_lines_backslash)

# .len()
# .isdigit() - if the string contains all digits
# .isalnum() - if contains number but without spaces (and spec chars?)
print(iron_man.isalnum())
iron_man_wo_spaces = iron_man.replace(' ','')
iron_man_wo_spaces = iron_man_wo_spaces.replace("'",'')
iron_man_wo_spaces = iron_man_wo_spaces.replace('''"''','')
print(iron_man_wo_spaces)
print(iron_man_wo_spaces.isalnum())
# .isalpha() - if all are character without spaces and commas...
# .upper() .lower()
# .isspace() - if all content is a space
print(' \t\n '.isspace())
print('\t\n'.isspace())
print('\f'.isspace())
print('\u2005'.isspace())
# .startswith() .endswith() find()
# .replace()
# .split()
# .join()
iron_man_w_spaces = "I am Iron Man"
print('-'.join(iron_man_w_spaces))
# .strip() .swapcase() .title() .capitalize()
GOTG = 'I am Groot'
print(GOTG.swapcase())
print(GOTG.title())
print(GOTG.capitalize())
# ord() - convert a character to its ASCII or Unicode integer equivalent
#print(ord(GOTG)) # not working because it works only with a single char
print(ord('H'))
# chr() - convert an integer to its ASCII or Unicode character equivalent
print(chr(163))
print(chr(72))
# isprintable()

# String Concatenation
print('\nString Concatenation\n')

avenger = 'Tony' ' Stark'
print(avenger)
avenger_2 = " avenger"
print(avenger + avenger_2)
print(avenger * 2)

# Identity Operators - is, is not
# Membership Operators - in, not in
# Comparison Operators - <,>,==,!= - based on their alphabetical order position
print('\nIdentity Operators - is, is not\n')
print('Iron' < 'Tony')
print('Hulk' == 'hulk')
print('Hulk' != 'hulk')

# Logical Operators - and, or, not
# Empty string has a False value

# and
# - if the value on the left hand side is False (empty) the and operator will give the left side value is executed
# - if the value on the left is True, then the value on the right hand side will be executed
print("\nThe 'and' operator\n")
print('IronMan' and 'Steve') # 'Steve'
print('' and 'Tony') # ''
print('Steve' and '') #''

# or
# - if left hand side is True, then it will True or left hand side value
# - if left hand side is False, then the value on the right hand side will be executed
print("\nThe 'or' operator\n")
print('IronMan' or 'Steve') # 'IronMan'
print('' or 'Tony') # 'Tony'
print('Steve' or '') # 'Steve'

# not
# - will return the complemented output
# - if the string is empty (False), it will read as "not False", which is true
print("\nThe 'not' operator\n")
print(not('Tony')) # False
print(not('')) # True

# String Slicing
# [a:b]
print("\nString Slicing\n")
infinity_war = 'obambe'
print(infinity_war[1:3])

# Python String Formatters
# strings can be formatted using letter 'f' before writing the string
# and writing the variable in curly braces at that exact plase where it is written.
# or using %s (like %d for integers and %f for floating point numbers)
# or using .format() method
print("\nString Formatters\n")
name = 'SpiderMan'
city = 'NewYork'
#identity = f'I am {name} and I belong to {city}'
#identity = f'I am %s and I belong to %s' %(name,city)
#identity = 'I am {0} and I belong to {1}'.format(name,city)
#identity = 'I am {1} and I belong to {2}'.format(name,city) # not working
#identity = 'I am {} and I belong to {}'.format(name,city)
my_dict = {'name':'SpiderMan','city':'NewYork'}
identity = 'I am {name} and I belong to {city}'.format(**my_dict)
print(identity)

# .zfill() - add zeros to the begining of the string to have the width that added as input param
print("\n .zfill()")
print('Tony'.zfill(6))
print('Tony'.zfill(2))

# .center()
print("\n .center()")
print('Mark70'.center(10))
print('Mark70'.center(10,'-'))

# .rjust() .ljust()
print("\n .rjust()")
print('Mark70'.rjust(10))
print('Mark70'.rjust(10,'-'))
print('Mark70'.ljust(10,'-'))

# .rstrip() .strip()

# partition(<sep>) rpartition(<sep>)
richest_avenger = 'Tony@Iron@Man'
print(richest_avenger.partition('@'))
print(richest_avenger.rpartition('@'))

# .rsplit()
# .splitlines([<keepends>]) - split the string into lines and return them as list