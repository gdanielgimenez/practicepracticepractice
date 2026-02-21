#! python3
# an insecure password locker program
# as defined by the book this is the first 'chapter project' of the book.
import sys
import pyperclip


PASSWORDS = {'email': 'f7min987asdf98asd9f87a9987dfgh987dfgh98d7fg8h9',
             'blog': 'VMA741rfv8552gbyn85yu2',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There\'s no account named' + account)
