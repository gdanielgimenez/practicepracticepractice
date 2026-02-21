#! python3
# bulletpoint adder
# end of chapter 6 project 2

import pyperclip
text = pyperclip.paste()

# separate lines and add the stars
lines = text.split("\n")
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
#
text = '\n'.join(lines)
pyperclip.copy(text)

# tested working
