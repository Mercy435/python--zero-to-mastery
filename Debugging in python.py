# debugging
# do the following
# linting allows us to detect errors as we code.. the red underline by pyflakes
# use an ide or editors cos they have inbuilt formatting tools, pep8 standard
# read errors
# python debugger pdb is a builtin module in python

import pdb

def add(num1, num2):
    pdb.set_trace()  # gives an extra boost, takes u to an  interactive pdb environment where u can debug ur codes
    # print(num1,num2) can be used to debug code, helps u see whats wrong
    t= 4*5 # typing t gives u an error cos u are on set trace line, use step to move
    return num1 + num2


add(4, 'hhkads')
# help shows u documented commands in the pdb environment
# list shows all of ur codes u wrote
# help list shows u the documentation of list
# clear clears
# step allows u go to the next line of code
# continue allows u continue through the code till u return sth
# a gives u all the arguments of the current function we are in
# w shows the context of the current line we are executing
# exit exits
# we can change variables in the pdb environment. make the change e,g,num2=5 then do next
# now we can remove the pdb and make the corrections