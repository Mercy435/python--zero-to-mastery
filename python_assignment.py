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
while True:
    try:
        goals = input('what are your personal goals? ')
        while True:
            name = input('whats your name: first and last name? ')
            name.split(" ")
            first_name= name[0].isalpha()
            last_name=name[1].isalpha()
            if first_name and last_name:
                break
            else:
                print("enter a valid name")
                continue
        while True:
            month=input("input your month of birth in this format,Jan: ")
            month=month.capitalize()
            day = input("input your day of birth as a number: ")
            year = input("input your year of birth: ")
            DateOfBirth = month + ' ' + day + ', ' + year
            if month.isalpha() and len(month) == 3:
                if day.isnumeric():
                    if year.isnumeric():
                        break
                    else:
                        print('oops! not a valid year: ')
                        continue
                else:
                    print('please enter a valid number')
                    continue
            else:
                print('oops! month is not in the right format')
                continue
        while True:
            num= input("input the number of your street: ")
            street= input('whats your street in this form: bola close, fifth ave, alh street ')
            city = input("input your city of residence: ")
            street.split(" ")
            first_ = street[0].isalpha()
            last_= street[1].isalpha()
            address = num + ' ' + street + ', ' + city
            if num.isnumeric():
                if first_ and last_:
                    if city.isalpha():
                        break
                    else:
                        print('enter a valid city')
                else:
                    print('enter the correct street')
            else:
                print('input a correct city')
                continue
        while True:
            email = input('whats your email address? ')
            if '@' and '.com' in email:
                break
            else:
                print('email not in the correct format')
                continue
    finally:
        print(f"- Name: {name}\n- Date of birth: {DateOfBirth}\n- Address: {address}\n- Personal goals:{goals}\n"
              f"-email:{email}")
    break



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

# 8 contact book
class ContactBook:
    name = 'local'
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

person1=ContactBook('John', 'Arena', '08067899011', 'John@gmail.com')
print(person1.name)




    # using python csv module to write and save as it is better than txt
    def write_to_csv(data):
        with open('database.csv', mode='a', newline='') as database2:  # a to append
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])