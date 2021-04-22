# debugging
# do the following
# linting allows us to detect errors as we code.. the red underline by pyflakes
# use an ide or editors cos they have inbuilt formatting tools, pep8 standard
# read errors
print(26**2)
print(52**2)
print(2704/676)
def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
   #  w = word how do i remove first and last char
    return palindrome(w)

print(palindrome('rececar'))
