
import re

txt = "The rain in Spain"
# search  in Spain"
a = re.search('spain', txt)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())
# pattern = re.compile('search here')
# print(pattern.fullmatch(pattern)) # to compare two exact variables
x = re.search("\s", txt)
print(x)
print("The first white-space character is located in position:", x.start())
# findall- Returns a list containing all matches
# Return a list containing every occurrence of "ai":

x = re.findall("ai", txt)
print(x)
txt = "The rain in Spain"

# Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)  # returns an empty list

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")

txt = "That will be 59 dollars"

# Find all digit characters:

x = re.findall("\d", txt)  # returns all the digits in txt
print(x)

# split	Returns a list where the string has been split at each match
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)  # splits the first character
print(x)

# sub	Replaces one or many matches with a string
txt = "The rain in Spain"
x = re.sub("\s", "7", txt)  # replaces withspaces
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

pattern = re.compile(r'([a-zA-Z]).([a])')  # r stands for raw
string_ = 'search this inside of this text please! Mercy'
a = pattern.search(string_)
print(a)  # prints sea
print(a.group(1))  # prints s
print(a.group(2))  # prints a

# \d rep digits from 0 to 9

# email checker
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# str_ = 'b@b.com'
str_ = 'andrei'
a = pattern.search(str_)
b = pattern.search(str_)
print(a)  # matches
print(b)  # returns none

import re
# password checker
# @least 8 char long and contain any letter, numbers, $%#@, end with a number
password_checker = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
# r"[A-Za-z0-9$%#@]{8,}[0-9") is same as password checker above
# [A-Za-z0-9$%#@] - A-Z for cap, a-z for lower case, 0-9 for number, then the special characters u want
# {8,}\d -{8,} is for at least 8 char and \d is for any digit
password = 'hdjkahskdha5534%$92'
check = password_checker.fullmatch(password)
print(check)
