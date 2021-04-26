import re
txt = "The rain in Spain"
# search  in Spain"
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

#Find all digit characters:

x = re.findall("\d", txt) # returns all the digits in txt
print(x)

# split	Returns a list where the string has been split at each match
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1) # splits the first character
print(x)


# sub	Replaces one or many matches with a string
txt = "The rain in Spain"
x = re.sub("\s", "7", txt) #replaces withspaces
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)