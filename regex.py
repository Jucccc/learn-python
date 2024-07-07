import re

# replace all digits in a string with underscore
pattern = re.compile(r"") # it's a good practice to always start with this line before any logic
my_string = "as2f66nnm534"
#pattern = re.compile(r"[0-9]") # without '+' 123 is treated as 1,2 and 3
#pattern = re.compile(r"[0-9]+") # using '+' 123 is treated as a single character
pattern = re.compile(r"\d+") # [0-9] can also be replaced with \d

'''
Special sequences

.           matches any single character except newline character
\d          matches any digit [0-9]
\D          matches non-digit characters [^0-9]
\s          matches whitespace character [\t\n\r\f\v]
\S          matches non-whitespace character [^\t\n\r\f\v]
\w          matches alphanumeric character [a-zA-Z0-9_]
\W          matches non-alphanumeric character [^a-zA-Z0-9]
\A          returns a match if the specified characters are at the
                beggining of the string
\b          returns a match where the specified characters are at
                the beggining or at the end of a word
\B          returns a match where the specified characters are present,
                but NOT at the beginning (or at the end) of a word
\Z          returns a match if the specified characters are at the
                end of the string

                
Quantifiers - simply specify the quantity of characters to match

Quantifier  Description         Example     Sample match
+           one or more         \w+         ABCDEF097
{2}         exactly 2 times     \d{2}       01
{1,}        one or more times   \w{1,}      smiling
{2,4}       2,3 or 4 times      \w{2,4}     1234
*           0 or more times     A*B         AAAAB
?           once or none        \d+?        1 in 12345


Sets - is a set of characters inside a pair of square brackets []
        with a special meaning

[arn]       returns a match where one of the specified characters (a,r or n) are present
[a-n]       returns a match for any lower case character, alpabetically between a and n
[^arn]      returns a match for any character EXCEPT a,r, and n
[0123]      returns a match where any of the specified digits (0,1,2 or 3) are present
[0-9]       returns a match for any digit between 0 and 9
[0-5][0-9]  returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]    returns a match for any character alphabetically between a and z, lower case OR upper case
[+]         In sets, +,*,.,|,(),$,{} has no special meaning, so [+] means: return a match for any + charater in the string

'''

#pattern = re.compile(r"\D+") # will replace the non-digit characters
#pattern = re.compile(r"[^0-9]+") # same as previous row
result = pattern.sub("_",my_string) # my_string will be checked for a pattern
                                    # wich is defined in the previous row
print(result)

pattern = re.compile(r"\d+")
result = pattern.findall(my_string)
#result = re.findall("\d+", my_string) # same as previous
print(result)

# Verify the first letter of input string is correct
my_string = "Bond! James Bond 007"
result = re.findall(r"^Bond", my_string) # The ^ means here: first letter.
                                        # In Sets (inside square brackets), it means negation.
if (result):
    print("The string starts with 'Bond'")
else:
    print("No match")

# Check the last letter
if (re.findall(r"007$", my_string)):
    print("The string ends with '007'")
else:
    print("No match")

# Verify the first letter of input string is correct as it was entered,
# without using ^ operator

my_string = "patience is the key to success"
result = re.findall(r"\A[Pp]atience",my_string)
print(result)
if (result):
    print("The string starts with 'Patience' or 'patience'")
else:
    print("No match")

# Search for a given word of input string and also verify its position
my_string = "The truth is... I am The Iron Man"
result = re.search("The", my_string) # returns a Match object. If there is more than one match,
                                # only the first occurance of the match will be returned
                                # 'findall' will return all the occurance
print(result)
print(result.span())
print(result.group())
result = re.findall("The", my_string)
print(result)
if (result):
    print("'The' is in the input string")
else:
    print("No match")

# Split function

my_string = "The name is cable"
result = re.split(r"\s", my_string)
print(result)
result = re.split(r"\s", my_string, 2)
print(result)

# Search for an upper case character in the beginning of a word, and print its position

my_string = "I am Iron Man"
result = re.search(r"\bI\w+", my_string)
print(result.span())
print(result.group())

# write a RegEx in walrus operator
text = ' Python 3.8 was released on 14-10-2019'
if (match_res := re.findall(r'[\d]{1,2}-[\d]{1,2}-[\d]{4}', text)):
    print('The matched result is:',match_res)