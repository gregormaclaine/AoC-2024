def is_diff_valid(diff: list[int]):
    if 0 in diff:
        return False
    sign = diff[0] // abs(diff[0])
    return all(d * sign > 0 and d * sign < 4 for d in diff)


def possibilities(diff: list[int]):
    yield diff
    for i in range(len(diff)):
        yield diff[:i] + diff[i + 1:]


with open('input/day-2.txt') as f:
    data = [line.split(' ') for line in f.read().strip().split('\n')]

    count = 0

    for line in data:
        vars = possibilities([int(x) for x in line])
        diffs = [[int(b) - int(a) for a, b in zip(line, line[1:])]
                 for line in vars]
        if any(is_diff_valid(d) for d in diffs):
            count += 1

    print(count)
