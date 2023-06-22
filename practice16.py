import re

s = "red flag is not blue flag, blue flag is not red flag, all red flag blue falg is not a green flag"
c = re.findall('(red flag | blue flag)', s)
print(c)
