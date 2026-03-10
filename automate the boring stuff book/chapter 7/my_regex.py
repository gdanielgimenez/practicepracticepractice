# own shorter version of no_regex
# finding a phone number in a string
# the pattern we'll be looking for 3 numbers hyphen  3 numbers hyphen 4 numbers.
# 555-555-4123


def isPhoneNumber(text):
    """searches for a pattern in a string"""
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-' and text[7] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return f"{text}  is a number"


def phoneNumber(message):
    """checkfing phone pattern in larger strings"""
    if len(message) > 12:
        for i in range(len(message)):
            chunk = message[i:i+12]
            if isPhoneNumber(chunk):
                print(f"Phone number found {chunk}")
        print('Done')
    else:
        print(isPhoneNumber(message))


# function calls
print("415-555-4242 is a phone number : ")
phoneNumber("415-555-4242")
print("Moshi moshi is a phone number : ")
phoneNumber(("Moshi moshi"))
# testing larger strings
message = 'Call me at 415-555-4242 tomorrow. 415-555-9999 is my office.'
phoneNumber(message)
