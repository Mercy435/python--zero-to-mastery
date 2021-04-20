# import utility

# print(utility)
# import shopping.more_shopping.shopping_cart

# print(shopping.more_shopping.shopping_cart.buy('apple'))
# a simpler way to do 4-6 above is using from, import the function

# from shopping.more_shopping.shopping_cart import buy
# print(buy('apple'))

# from utility import multiply, divide, max
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
'''
import sys
print(sys)  # built in module
sys.argv

# gaming guess exercise
from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if  0 < guess < 11:
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

x = platform.system()
print(x)
