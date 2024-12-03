def is_diff_valid(diff: list[int]):
    if 0 in diff:
        return False
    sign = diff[0] // abs(diff[0])
    return all(d * sign > 0 and d * sign < 4 for d in diff)


with open('input/day-2.txt') as f:
    data = [line.split(' ') for line in f.read().strip().split('\n')]
    diffs = [[int(b) - int(a) for a, b in zip(line, line[1:])]
             for line in data]
    print(len([d for d in diffs if is_diff_valid(d)]))
