#regex2.py
import re

pattern = r'abc'
regex = re.compile(pattern)

match_obj = regex.search('abcdefabc')

print(match_obj.pos)
print(match_obj.endpos)
print(match_obj.re)
print(match_obj.string)
print(match_obj.lastgroup)
print(match_obj.lastindex)
print('===========================')


print(match_obj.start())
print(match_obj.end())
print(match_obj.span())