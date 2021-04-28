# 1
'''
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

#2
input_ = input('Whats on your mind today?: ')
separate = input_.split(' ')
word_count = len(separate)
print(f"oh nice, you just told me what's on your mind in {word_count} words!")
'''
with open(r'C:\Users\Isaac Alexander\Desktop\test.txt', mode='r') as my_file:
    content = my_file.read()
    print(content)
    slit = content.split(' ')
    length = len(slit)
    print(f"oh nice, you just told me what's on your mind in {length} words!")




