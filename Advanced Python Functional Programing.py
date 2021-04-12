def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))  # this is a pure function


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    print(new_list)  # this interacts with the screen, it has side effect.the print statement.. this not a pure function


multiply_by2([1, 2, 3])

new_list = []


def multiply_by2(li):
    for item in li:
        new_list.append(item * 2)
    print(new_list)


multiply_by2([1, 2, 3])  # this is not pure, it interacts with new_list outside the world of the function
# new_list can be changed

wizard = {'name': 'Merlin', 'power': 50}  # this is the data


def attack(li):  # this isn't a method but a function cos its outside a class, it can take any parameter
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


# common and useful functions
# map,filter,zip,reduce
# map helps simplify codes, you dont need to create an empty list or append to a list, or call the function
def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, [1, 2, 3])))  # use list to show the output

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))
print(my_list)

# filter selects based on a certain condition
my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)

# zip merges two iterables together
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)

print(list(zip(my_list, your_list, their_list)))

# reduce- this is not a built in function, it is imported from functools module
from functools import reduce

my_list = [1, 2, 3]  # reduce reduces the list to 6


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print((reduce(accumulator, my_list, 0)))  # o is the initial value(acc) we want, default is 0

my_list = [1, 2, 3]  # reduce reduces the list to 16


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print((reduce(accumulator, my_list, 10)))

# lambda expressions used for expressions or functions we will use once and theres no need to store in memory
# lambda param: action(param)
my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

# lambda exercises
# 1. square items in a list using lambda
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

# 2. LIST SORTING
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

# list/set/dict comprehensions - quick way to create these datatypes instead of looping
# my_list = [char for char in iterable]
my_list = [char for char in 'hello']
print(my_list)
my_list2 = [num for num in range(0, 100)]
print(my_list2)
my_list3 = [num * 2 for num in range(0, 100)]
print(my_list3)
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]  # generate list of even numbers=
print(my_list4)

my_set = {char for char in 'hello'}  # not l is not repeated
print(my_set)
my_set1 = {num for num in range(0, 100)}
print(my_set1)

simple_dict = {'a': 1, 'b': 2}
my_dict = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)

my_dict1 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict1)

# exercise on comprehensions
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
list_ = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in list_:
            list_.append(item)
print(list_)

duplicates = {item for item in some_list if some_list.count(item) > 1}
#duplicates = set([item for item in some_list if some_list.count(item) > 1])
print(list(duplicates))
