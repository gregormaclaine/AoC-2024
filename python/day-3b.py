import re


def mul(a, b):
    return a * b


with open('input/day-3.txt') as f:
    matches = re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do(n\'t)?\(\))', f.read())

    enabled = True
    count = 0
    for m in matches:
        if m[0] and enabled:
            count += eval(m[0])
        elif m[2]:
            enabled = False
        elif m[1]:
            enabled = True

    print(count)
