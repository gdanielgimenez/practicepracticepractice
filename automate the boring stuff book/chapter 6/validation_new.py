# changing the validation.py example for a less convoluted code
# by using regex
import re
# we first create the regex to validate user input
# at least 8 chars numeric words and special char
# for this case every check will have to be separated to say for example
# missing an uppercase character, missing a number etc
lowerCaseRegex = re.compile(r'[aeiou]')
upperCaseRegex = re.compile(r'[AEIOU]')
numRegex = re.compile(r'[0-9]')
# test if it works with just /d as well
# shorter version of a special char
specialCharRegex = re.compile(r'[!@#]')


print('Type a new password : ')
print('At least 8 characters long \n1 lower case char \none upper case char \none number'
      '\none special char')
#
while True:
    password = input()
    if len(password) < 8:
        print('password must be at least 8 characters long')
    elif lowerCaseRegex.search(password) == None:
        print('password requires at least one lower case letter')
    elif upperCaseRegex.search(password) == None:
        print('password requires at least one upper case letter')
    elif specialCharRegex.search(password) == None:
        print('password requires at least one special character')
    else:
        print(f"{password} testing if password is valid")
        print('password is valid.')
        break
