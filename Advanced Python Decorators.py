def hello():
    print('helllloooooo');


greet = hello()  # prints helllloooooo'
greet = hello  # shows where hello is in memory
del hello  # deletes the name hello not the function cos greet is pointing to it

print(greet())


def hello(func):
    func()


def greet():
    print('still here!')


a = hello(greet)
print(a)


# HIGHER ORDER FUNCTION HOC
# a function that accepts another function
def greet(func):
    func()


# or  a function that returns another function
def greet2():
    def func():
        return 5

    return func


# map(), reduce, filter are HOC


# decorator act like variables, it supercharges a function
# Decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        # print('**********')
        func(*args, **kwargs)
        # print('**********')

    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


hello('greeting')


# @my_decorator # 1 this is preferable
def bye():
    print('see ya later')


hello2 = my_decorator(bye)  # my_decorator receives a function and wraps it in  # 2


# hello2()

# my_decorator(bye)()  # 3


# performance decorator exercise
def performance(fn):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time() # current time
        print(t1)
        result = fn(*args, **kwargs)
        t2 = time() # time after code is ran
        print(t2)
        print(f'it took {t2 - t1}s')  # it took 0.20325016975402832ms to get result
        return result

    return wrapper

# applying decorator to function
@performance
def long_time():
    for i in range(10000000):
        i * 5


long_time()

# authenticator decorator exercise
# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:


user1 = {'name': 'Sorna', 'valid': True}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
