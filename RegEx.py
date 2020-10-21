# Regular Expressions:
import re

string = 'search inside of this text please!'
e = (re.search('this', string))
print(a.span())
print(a.start())
print(a.end())
print(a.group())

pattern = re.compile('Search inside this text please!')

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

import re

pattern = re.compile(r"([a-zA-Z]).([a])a")

string = 'search inside of this text please!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.group(2))
