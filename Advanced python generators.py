# generators allow us generate sequence of values over time. uses keyword yield and it can pause and resume functions
# range is a generator,
'''
range(100)
list(range(100))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)  # this takes up space in  memory
print(my_list)


# a generator(range) is a subset of an iterable(list, range)

def generator_function(num):
    for i in range(num):
        yield i  # pauses the function till when we do sth to it again


for item in generator_function(1000):
    print(item) # prints one by one



# calling the function
def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(100)
print(g)  # shows us a generator function in memory
# next is used to resume the function yield paused
print(next(g))  # this gives 0, first item in range 100
next(g)  # 0 0 *2
next(g)  # 1 1*2next(g)
next(g)  # 2 2*2


# once the num of range has been exceeded, calling next gives a stop iteration error

# generator performance
def performance(fn):
    from time import time
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1}s')  # it took 0.20325016975402832ms to get reult
        return result

    return wrapper


@performance
def long_time():
    print('1')
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i * 5


long_time()
long_time2()

# with generators we dont have to hold things in memory and hence perform things quickly
# generators are useful in calculating large set of data
# generators are faster than list when we want to loop a large range of data
def gen_fun(num):
    for i in range(num):
        yield i

for item in gen_fun(100)


# under the hood of generators
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)  # do a print to see the actual values
        except StopIteration:
            break


special_for([1, 2, 3])  # objects exist in the same memory space


# creating your special range in python
class MyGen():
    current = 0 # class object attribute

    def __init__(self, first, last):
        self.first = first
        self.last = last
# using dunder methods
    def __iter__(self): # helps us create an iterable
        return self

    def __next__(self): # current helps us remember where we are as next does
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)



# fibonacci exercise
#1. using generators
def fib(number):
    current = 0
    previous = 1
    for i in range(number):
        yield current
        temp = current
        current = previous
        previous = temp + previous


for item in fib(200):
    print(item)
'''


# 2 using list
def fib2(number):
    current = 0
    next_ = 1
    result = []
    for i in range(number):
        result.append(current)
        temp = current
        current = next_
        next_ = temp + next_
    return result


print(fib2(20))
