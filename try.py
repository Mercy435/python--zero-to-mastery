domain_names = {'Google': 'gmail', 'Yahoo': 'yahoo', 'MyFantasy': 'myfantasy',
                'Microsoft': 'outlook'}
email = input('enter a valid email address: ')
# d = email[email.index('@') + 1:]
# print(d)

a = email.split('@')[1]
# print(a)  # this splits the email in two, the first half is index 0 and the other is index 1
b = a.split('.')[0]
# print(b)
# if b == domain_names.value():
# key = domain_names[b]
# print(key)

# 7 email slicer
domain_names = ['Google', 'MyFantasy', 'Microsoft', 'Yahoo']
email = input('enter a valid email address: ')
split_email = email.split('@')[1]
name = email.split('.')[0]
split_domain_name = split_email.split('.')[0]
if split_domain_name == 'gmail':
    print(f"Hey {name}, I see your email is registered with {domain_names[0]}. That's cool!.")
elif split_domain_name == 'myfantasy':
    print(f"Hey {name}, looks like you've got your own custom setup at {domain_names[1]}. Impressive!")
elif split_domain_name == 'outlook':
    print(f"Hey {name}, I see your email is registered with {domain_names[2]}. That's cool!.")
else:
    print(f"Hey {name}, looks like you've got your own custom setup at {domain_names[-1]}. Impressive!")

import re

a = re.findall('[\w-]+@[\w-]+', email)
# print(a)
