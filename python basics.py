'''
#password checker
user_name = input('What is your username? ')
password = input('What is your password? ')
password_length = len(password)
hidden_password = '*' * password_length
print(f'Hey {user_name}, your password, '
      f'{hidden_password}, is {password_length} letters long')

#gaming exercise using conditional logical operators
is_magician = False
is_expert = True
if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("you need magic powers")
#looping over a dictionary
user = {'name': 'Golem', 'age': 5006, 'can_swim': False}
for item in user:
    print(item) #this prints the keys
for item in user.keys():
    print(item)
for item in user.items(): #returns keys
    print(item) #this returns the keys and values in a tuple
for item in user.values():
    print(item) #this returns the values
for key, value in user.items():
    print(key, value) #returns keys and values not in a tuple

#counter exercise
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for i in list_:
    counter += i
print(counter)
'''

for _ in range(10, 0, -2):
    print(list(range(10)))

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50: {i}')

my_list = [1, 2, 3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

#graphical user interface GUI
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
#1. iterate over picture.
# if o, print ''
# if 1 print *
for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('') #need a new line after every loop

#check for duplicates in a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

#parameters are used when we define a function
def say_hello (name, emoji):
    print(f'helllllooooo {name} {emoji}')

#arguments are used when we call a function
#say_hello(('andrei', 'smily'))

def is_even(num):
    return num % 2 == 0

print(is_even(51))

def super_func(*args): #this allows more than one argument
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))

def highest_even(list_):
    evens = []
    for i in list_:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)

print(highest_even([10,2,3,4,5,11]))
print()
