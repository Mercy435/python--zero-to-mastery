# 1

while True:
    try:
        user_input = input('enter a number you are thinking or enter q to exit: ')
        if user_input == 'q':
            break
        else:
            if 0 < int(user_input) < 1000:
                if int(user_input) % 2 != 0:
                    print("That's an odd number! Have another? ")
                else:
                    print("That's an even number! Have another? ")
            else:
                print('please enter a number between 1 and 1000')
    except ValueError:
        print('please enter a number')

# 2
input_ = input('Whats on your mind today?: ')
separate = input_.split(' ')
word_count = len(separate)
print(f"oh nice, you just told me what's on your mind in {word_count} words!")

with open(r'C:\Users\Isaac Alexander\Desktop\test.txt', mode='r') as my_file:
    content = my_file.read()
    print(content)
    slit = content.split(' ')
    length = len(slit)
    print(f"oh nice, you just told me what's on your mind in {length} words!")

# 3

try:
    name = input('whats your name? ')
except ValueError:
    print('enter a valid value')
    # dob = input('whats your date of birth? ')
    # address = input('whats your address? ')
    # goals = input('what are your personal goals? ')
    # email = input('whats your email address? ')
# except ValueError:
#     print('please enter a valid value')
# try:
#
# except TypeError:


# 4 acronym
acronym_derivative = (input('enter the full meaning of an organization or concept: '))
output = acronym_derivative.split()
# print(output)
placeholder = ''
for word in output:
    print(placeholder + word[0].upper(), end='')

print('\n')

# 5 guess the number
from random import randint

correct_guess = randint(1, 50)
# print(correct_guess)
attempts = 0
while True:
    try:
        number = int(input('guess a number between 1 and 50: '))
        if 0 < number < 51:
            attempts += 1
            if number == correct_guess:
                print(f'congratulations!, you guessed the right number after {attempts} attempts')
                break
            else:
                print('Do you want to keep playing or would you like to quit?.')
                choice = input('')
                if choice == 'i want to keep playing':
                    continue
                elif choice == 'i will like to quit':
                    print('press q to quit')
                    response = input(':')
                    if response == 'q':
                        break
                    else:
                        print("you've typed the wrong command")
                        # ask kelvin
                else:
                    print('input the correct message')
                continue
        else:
            print("oops!,that's outside the range")
    except ValueError:
        print('please input a valid number')

# 6
word_input = input('give me five words:')
each = word_input.split()
for word in each:
    if word == word[::-1]:
        print(word)

# 7 email slicer
domain_names = ['Google', 'MyFantasy', 'Microsoft', 'Yahoo']
email = input('enter a valid email address: ')
split_email = email.split('@')[1]
name = name = email.split('.')[0]
split_domain_name = split_email.split('.')[0]
if split_domain_name == 'gmail':
    print(f"Hey {name}, I see your email is registered with {domain_names[0]}. That's cool!.")
elif split_domain_name == 'myfantasy':
    print(f"Hey {name}, looks like you've got your own custom setup at {domain_names[1]}. Impressive!")
elif split_domain_name == 'outlook':
    print(f"Hey {name}, I see your email is registered with {domain_names[2]}. That's cool!.")
else:
    print(f"Hey {name}, looks like you've got your own custom setup at {domain_names[-1]}. Impressive!")

# 8
