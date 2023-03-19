import re

s = str(input())
a = bool(re.match(r'[^z]*z[^z]{3}z[^z]*', s))
if a == True:
  print(s)
else:
  print("no find")
