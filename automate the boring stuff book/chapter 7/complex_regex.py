# page 164
# managing complex regex with with re.VERBOSE
import re
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

examples = [
    "415-555-1234",          # dashes
    "(415) 555 1234",        # parens + spaces
    "415.555.1234",          # dots
    "555-1234",              # no area code
    "415-555-1234 ext 99",   # with extension
    "(800) 555.1234 x1234",  # parens + dots + x extension
    "415 555-1234 ext.123",  # space separator + ext.
]
# first line takes the area code, which may or may not be included => ?
# area code can be 3 bare digits 555 or can be 3 digits in (555)

# second line separator also may or may not be included if area code
# separator coulbd be whitespace or a dash or a dot .

# third line is just 3 digits

# fourth line is another separator white space or dash or dot

# fifth line white space followed by either ext or x or ext.
# either one shorthand for extension followed by whitespace or not
# and 2 to 5 digits

# Combining re.IGNORECASE re.DOTALL and re.VERBOSE
# re.IGNORECASE  to make the regex object match case-insensitive
# re.DOTALL makes . change the default behavior and includes new line
# re.VERBOSE makes it possible to split the regex in multi line and ignore white spacing

# all 3 can be combined using the pipe character |
# for a regular expression  that's case insensitive and  includes new lines
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
# and finally we could add the verbose option for multiline
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
