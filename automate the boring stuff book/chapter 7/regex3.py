# we can also substitute strings with the sub() method
# we get in return the updated string
import re
namesRegex = re.compile(r'Agent \w+')
newString = namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(newString)

# we could also re-use part of the string return something like Agent ****
cenRegex = re.compile(r'Agent (\w)\w*')
agentNames = cenRegex.sub(
    r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
print(agentNames)
