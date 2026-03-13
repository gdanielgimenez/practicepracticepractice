import re
# we can think of the ? as matching zero o one

# matching zero or more with the star *
batRegex = re.compile(r'Bat(wo)*man')
# as previously seen this will work with batman batwoman but also
mo1 = batRegex.search('the adventures of Batwowowoman')
print(mo1.group())
# it works with batwowowoman because the stars signifies it'll match not matter
# how many times wo is repeated within Bat-man in this case

# matching one or more with PLUS +
batRegex2 = re.compile(r'Bat(wo)+man')
# for this case we'll find matching objects for Batwoman (1 wo) and for
# Batwowowoman (3 wo) but will not work for Batman
mo2 = batRegex2.search('the adventure of Batwoman')
print(mo2.group())

# matching specific repetitions with curly braces
haRegex = re.compile(r'(Ha){3}')
moho = haRegex.search('HaHaHa')
# group should return the value but Hahaha would NOT be returned
print(moho.group())

# greedy and non-greedy matching
# greedy matching is the default behavior what it means is in the ambiguos case
# of having a 3-5 match it will always match the longer string
# this regex match from 3 to 5 repetitions
greedyRegex = re.compile(r'(Ha){3,5}')
momo = greedyRegex.search('HaHaHaHaHa')
print(momo.group())
# should return 5 repeats
nonGreedyRegex = re.compile(r'(Ha){3,5}?')
momo = nonGreedyRegex.search('HaHaHaHaHa')
print(momo.group())
# should return HaHaHa as is the shortest string match
# note that the question mark can have two meanings in regular expressions
# declaring a non-greedy match or flagging an optional group

# the findall() method
# we previously saw that matching objects search by default returns only the first
# findall() does not return a match object but instead a list of strings
PhoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
allnumbers = PhoneNumberRegex.findall(
    'cell: 415-555-424242 work: 212-555-0000')
print(allnumbers)
# when we have groups (\d\d\d-)-\d\d\d-\d\d\d\d
# we instead get in return a list of tupples corresponding to each phone number
phoneNumReg = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups ()
phoneNR = phoneNumReg.findall('cell: 415-555-424242 work: 212-555-0000')
print(phoneNR)


# useful Character classes
# \d     any numeric digit from 0 to 9
# \D     any character that is NOT numeric digit from 0 to 9
# \w     any letter numeric digit or underscore (this of this as match "words")
# \W     any character that is NOT letter numeric digit or underscore (this of this as match " not words")
# \s     any space tab or newline (think of this as matching space)
# \S     anything that is NOT space tab or newline

# square brackets can be use to define shorthand versions of custom matches like [0-5]
# instead of writing (1|2|3|4|5) both will only match numbers between 0-5

# we can create regex to fit whatever sort of need we have
# given an example for a christmas presents list

xmasRegex = re.compile(r'\d\s\w+')
# this regex matches a string that starts with a digit (0-9) followed by space
# and finally a "word" "00 something" would be a match
presents = xmasRegex.findall(
    '12 toys, 5 socks, 3 shirts, 2 phones, 1 computer')
print(presents)

# making your own character classes
# REGEX for all vowels lowercase and uppercase
vowelRegex = re.compile(r'[aeiouAEIOU]')
# we can also include ranges for letters or numbers by using a hyphen
volNumRegex = re.compile(r'[a-zA-Z0-9]')
# this character class regex will match all lower case and uppercase letters
# from a to z and all numbers from 0  to 9
# when we use square brackets to define class we dont need escape characters
# the caret ^ caracter transforms a regular character class to a negative one
# if we want to match all NON-vowels characters we would change our previous
# example with a caret at the beginning like so
nonVowelsRegex = re.compile(r'^[aeiouAEIOU]')

# when we want to make an exact match from beginning to end both ^ $
# the caret by it self signals ^\d what the string should begin with
# and the $ by itself signals $\d we are looking for a match ending with
# but when we combine the two it matches exactly a start and an end
beginsHelloReg = re.compile(r'^Hello')
thisPass = beginsHelloReg.search("Hello World")
thisFails = beginsHelloReg.search("he said Hello")
# for the $ match ending with a digit or more
endsWithNum = re.compile(r'\d+$')
thisPass = endsWithNum.search("Your number is 42")
thisFails = endsWithNum.search("your number is forty two")
#
# when we combine the 2 ^ $
wholeStringIsNum = re.compile(r'\d+$')
# this regex matches strings that both begin and end with one or more numeric char
# this pass '1234567890'
# this fails '12345xyz890'
# this also fails '12  3457890'

# the wild character .(dot)
# this regex matches words that have at
atRegex = re.compile(r'.at')
atat = atRegex.findall('The cat in the hat sat on the flat mat.')
print(atat)
# the . wildcard only matches one char thats why atat retunrs lat instea of flat

# matching everything with Dot-Star
# for a case where we would want to match something like the data from a
# First Name: name Last Name : lastname situation
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# this would return Al Sweigart
# where group1(Al) and group2(Sweigart)
# the .* is greedy by default but we can change its behavior with ?
#  greedy version r'<.*>'
# will match '<To serve a man> for dinner.>'
# non-greedy version r'<.*?>'
# will match only '<To serve a man>'

# matching new lines with Dot character
noNewLineReg = re, compile('.*')
# matches everything before a new line, which . doesnt include by default.
newLineReg = re.compile('.*', re.DOTALL)
# will match everything even new lines

# case insensitive matches
# re.IGNORECASE or re.i
robocopRe = re.compile(r'roboco', re.i)
robocopRe = re.compile(r'roboco', re.IGNORECASE)
# no matter which of the two versions we use now we'll be able to match
# robocop ROBOCOP Robocop RoBoCoP and everything in between
