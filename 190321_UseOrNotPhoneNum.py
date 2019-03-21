import re

s = input()

p1 = "(010)\D?\d{4}\D?(\d{4})"

m1 = re.search(p1, s) is not None

print(m1)