import re


def mul(a, b):
    return a * b


with open('input/day-3.txt') as f:
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', f.read())
    print(sum(eval(m) for m in matches))
