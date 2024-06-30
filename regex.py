import re

# replace all digits in a string with underscore
pattern = re.compile(r"") # it's a good practice to always start with this line before any logic
my_string = input("Enter a string: ")
#pattern = re.compile(r"[0-9]") # without '+' 123 is treated as 1,2 and 3
#pattern = re.compile(r"[0-9]+") # using '+' 123 is treated as a single character
pattern = re.compile(r"\d+") # [0-9] can also be replaced with \d
result = pattern.sub("_",my_string) # my_string will be checked for a pattern
                                    # wich is defined in the previous row
print(result)

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

