# regex (regular expressions)
import re
# creating the regex Object for the phone number format
# 444-555-4242 where \d represents a digit

# whenever we want to mathc something we need to create a regex object first
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# to test our previos example
phone_number = phone_regex.search('My number is 415-555-4242.')
print('Phone number found : ' + phone_number.group())

# we can do grouping with parenthesis ()
phone_regex_two = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# grouping returns a tupple and we can use several methods to get the same values

mo = phone_regex_two.search('My number is 415-555-4242.')
print("area code : ")
print(mo.group(1))
print("phone number : ")
print(mo.group(2))
# giving a value zero to group or no value at all returns everything
print(mo.group(0))
print(mo.group())
# we can also ask for the whole group and it returns the tupple
print(mo.groups())
# we could also do multiple assign to extract each of the values
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# if you need to match actual parenthesis use escape char
phone_regex_three = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phone_regex_three.search('My phone number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))
