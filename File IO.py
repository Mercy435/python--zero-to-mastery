'''
my_file = open('test.txt')


print(my_file.read)
# open to open the file
# read to read the contents of the file
#  can only read the file once.. to do  a read multiple times to show content of files, do
my_file.seek(0)
print(my_file.read)
# python uses the idea of a cursor to read files

print(my_file.readline())
# prints contents of a file per line,,, do it multiple times for the no of lines u want to view

print(my_file.readlines())
# gives a list containing all of the contents of the file

my_file.close() # closes the file

# standard way to read a file

with open('test.txt', mode='r') as my_file: # mode=r is for reading , its default
    print(my_file.readlines())

with open('test.txt', mode='r+') as my_file: # to read files and write to the file
    text = my_file.write('hey it\'me!') # to write to a file
    print(my_file.readlines())

with open('test.txt', mode='a') as my_file: # a stands for append.. it appends to the end of the file
    text = my_file.write('hey it\'me!') # to write to a file
    print(my_file.readlines())
# mode = w helps to write in the code

# to create a file that doesnt exist
with open('sad.txt', mode = 'w') as my_file:
    text = my_file.write(':(')


#file path
# to access  a file in a folder u can copy from the root user
with open('name_of_folder\name_of_file.txt', mode = 'r') as my_file:
    text = my_file.read()

with open('./app/sad.txt', mode = 'w') as my_file: #current directory
    text = my_file.write(':(')

with open('../app/sad.txt', mode = 'w') as my_file: #go one directory back
    text = my_file.write(':(')

#pathlib is  an object oreinted file system, a built in module

# file errors
# use the try block
try:
    with open('sad.txt', mode='r') as my_file:
        text = my_file.read()
except FileNotFoundError as err:
    print('file does not exist')
    raise err # gives FileNotFoundError
except IOError as err:
    print('IO error')
    raise err
'''
# translator exercise
from translate import Translator

translator = Translator(to_lang='ja')  # ja for japanese
try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-ja.txt', mode='w') as my_file2: # to create a new file to store the translation
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path')
