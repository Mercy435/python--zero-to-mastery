# error handling
# age = int(input('what is your age? ')) # using the int makes sure input is integer or convertible to int
# print(age)
# to handle error if wrong input is given(value error.. to make it keep running till a valid number is
# imputed use while loop

while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except:
        print('please enter a number')
    # to break out of the loop when a valid response is given do this
    else:
        print('thank you!')
        break

# use the except block to specify error type to handle
while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    # to break out of the loop when a valid response is given do this
    else:
        print('thank you!')
        break
# note that if u have two except blocks with same kind of error only the first will be considered, cos it goes back
# to the while loop


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:  # properly describe errors
        print(f"Please enter numbers {err}")


# print(sum('1', '2')) # this gives 12
print(sum('1', 2))  # this gives a type error


def sum_(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:  # wrapping errors
        print(err)


print(sum_(1, 0))
# use of finally
while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
        continue  # this goes back to the while loop
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you!')
        break
    finally:  # this runs regardless at the end of everything
        print('ok, i am finally done')
    print('can you hear me')

# raising your error
while True:
    try:
        age = int(input('what is your age? '))
        10 / age
        # raise ValueError('hey cut it out') # to throw in ur own error message
        raise Exception('hey cut it out')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    # to break out of the loop when a valid response is given do this
    else:
        print('thank you!')
        break
