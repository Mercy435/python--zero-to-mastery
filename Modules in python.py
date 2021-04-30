# import utility

# print(utility)
# import shopping.more_shopping.shopping_cart

# print(shopping.more_shopping.shopping_cart.buy('apple'))
# a simpler way to do 4-6 above is using from, import the function

# from shopping.more_shopping.shopping_cart import buy
# print(buy('apple'))

# from utility import multiply, divide, max
'''
from utility import *  # this imports all functions in utility

print(divide(5, 2))
print(multiply(5, 2))
print(max())  # this overrides the existing function max in python
# importing the entire module from the package
from shopping.more_shopping import shopping_cart

print(shopping_cart.buy('apple'))

# be explicit when importing modules
# print(__name__)  # this prints __main__, it is given specifically to he file we run
if __name__ == '__main__':
    print('please run this')
# the above checks for the main file to run code,, to check if modules are imported or ran


# python built in modules
import random

print(random)
# help(random)
print(dir(random))  # prints methods, do a . to see them too
print(random.random())  # gives a random no/ float btw 0 and 1
print(random.randint(1, 10))  # random no btw 1 and 10
print(random.choice([1, 2, 3, 4, 5]))  # prints a random no from a seq

# import random as oul
my_list = [1, 2, 3, 4, 5]

random.shuffle(my_list)
print(my_list)

# from random import shuffle
import sys

print(sys)  # built in module
sys.argv
#sys module
import sys
first =sys.argv[1]
last =sys.argv[2]

print(f'hiiiiiii! {first}, {last}'

# gaming guess exercise

# 1. generate a no from 1-10
from random import randint

answer = randint(1, 10)

# 2. input from user
# guess = int(input("guess a number 1-10: "))  # convert str input to int

# 3. check that input is a no from 1-10
# 4. check if no is the right guess, otherwise
# 5. ask user for input again

while True:
    guess = int(input("guess a number 1-10: "))
    try:
        # if guess > 0 and guess < 11:
        if 0 < guess < 11:
            if guess == answer:
                print("you are a genius!")
                break
        else:
            print('hey!, i said 1-10')
    except ValueError:
        print("please enter a number")
        continue # this goes back to the while loop
# give it ur start and last parameter using sys
'''
#using sys.argv you give the prgram the first and last parameters when u call it in the terminal
import sys
import random

answer = random.randint(int(sys.argv[1]), int(sys.argv[2])) #when calling the program on the terminal, pass 1 10

while True:
    try:
        guess = int(input("guess a number 1-10: "))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue



'''
import platform

x = platform.system()  # prints windows
print(x)

import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)  # prints a line of joke

# useful modules
from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))  # creates a dict or hashmap that keeps track of how many times an item occurs
sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

dictionary_ = {'a': 1, 'b': 2}
print(dictionary_['a'])

dictionary_ = defaultdict(int, {'a': 1, 'b': 2})
print(int())

dictionary_ = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary_['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)  # returns false

# date module
import datetime

print(datetime.time())  # returns 00:00:00
print(datetime.time(5,45,2))  # returns 05:45:02
print(datetime.date.today())  #  returns today's date

from time import time

from array import array
# an array is used to optimize list and saves array
arr = array('i', [1,2,3])
print(arr)
print(arr[0])

import mercy as m
print(m.my_name())
'''