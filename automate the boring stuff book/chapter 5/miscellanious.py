# things that might come useful.
# page 110 setdefault() method for dictionaries
user = {'name': 'nano', 'age': 35}
# we pass a key and its value to the function and if it doesnt exist yet
# it creates the new k-v onto the dictionary if not returns the existing value
# for that key
user.setdefault('location', 'usa')
print(user)
# in command line note that after we made the call it returns the value we
# just pass it to add to the key, that might be a little confusing


# we can import pprint and pformat from the print module both can come in
# in handy when printing data from dict or nested dict.
