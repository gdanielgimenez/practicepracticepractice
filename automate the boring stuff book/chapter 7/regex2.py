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

# square brackets can be use to define shorthand versions of matches like [0-5]
# instead of writing (1|2|3|4|5) both will only match numbers between 0-5
