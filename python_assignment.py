# 1

while True:
    try:
        user_input = input('enter a number you are thinking or enter q to exit: ')
        if user_input == 'q':
            break
        else:
            user_input = int(user_input)
            if 0 < user_input < 1000:
                if user_input % 2 != 0:
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
    # print(f"oh nice, you just told me what's on your mind in {length} words!")
    print("oh nice, you just told me what's on your mind in", int(length),  "words!")

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
print(correct_guess)
attempts = 0
while True:
    try:
        number = int(input('guess a number between 1 and 50: '))
        if 0 < number < 51:
            attempts += 1
            if number < correct_guess:
                print('go higher')
            else:
                print('go lower')
            if number == correct_guess:
                print(f'congratulations!, you guessed the right number after {attempts} attempts')
                break
            else:
                print('Do you want to keep playing?.Enter y/n')
                choice = input('')
                if choice.upper() == 'Y':
                    continue
                else:
                    break
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
domain_names = {'gmail':'Google', 'myfantasy': 'MyFantasy','outlook': 'Microsoft', 'yahoo': 'Yahoo'}
email = input('enter a valid email address: ')
split_email = email.split('@')[1]
name = email.split('@')[0]
split_domain_name = split_email.split('.')[0]
if split_domain_name in domain_names.keys():
    print(f"Hey {name}, I see your email is registered with {domain_names[split_domain_name]}. That's cool!.")

else:
    print(f"Hey {name}, looks like you've got your own custom setup at {split_domain_name}. Impressive!")

# 7 contact book
class ContactBook:
    name = 'local'
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

person1=ContactBook('John', 'Arena', '08067899011', 'John@gmail.com')
print(person1.name)