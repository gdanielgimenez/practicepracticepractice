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
# also referred to as destructuring in React or js note to self
print(areaCode)
print(mainNumber)

# if you need to match actual parenthesis use escape char
phone_regex_three = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phone_regex_three.search('My phone number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))
# the pipe | can be used for matching multiple values
# but it matches the first value encounter
heroRegex = re.compile(r'Batman | robin')
mo1 = heroRegex.search('Batman and robin')
# in this case the match object return will consist of Batman only
print(mo1.group())
heroRegex2 = re.compile(r'robin | Batman')
mo2 = heroRegex2.search('robin and Batman')
# this returns robin only
print(mo2.group())


# say we wanted to match any of the following batman related values
# Batman Batmobile Batcopter Batbat all this strings start with Bat
batRegex = re.compile(r'Bat(man|mobile|copter|bat|cave)')
mobat = batRegex.search(('the adventures of Batman'))
print(mobat.group())
mobat2 = batRegex.search(('secrets of the Batcave'))
print(mobat2.group())

# for cases with optional matching we can use the ?
# wheter we want Batman or Batwoman
batRegex3 = re.compile(r'Bat(wo)?man')
mo4 = batRegex3.search('the adventures of Batman')
mo5 = batRegex3.search('the adventures of Batwoman')
print(mo4.group())
print(mo5.group())
# we can adapt this regex for numbers with or without area codes
noAreaPhone = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = noAreaPhone.search('My number is 415-555-4242')
print(mo.group())
# without area code, it should take both cases
momo = noAreaPhone.search('My number is 555-4242')
print(momo.group())
