#regular_findall.py
import re

l = re.findall('ab','abcdcdab')
print(l)

regex = re.compile('ab')
m = regex.findall('abcdcdab')
print(m)

