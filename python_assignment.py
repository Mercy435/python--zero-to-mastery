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



