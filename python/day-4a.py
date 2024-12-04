def count_in_line(line):
    count = 0
    for i, c in enumerate(line[:-3]):
        if c == 'X' and line[i:i + 4] == 'XMAS':
            count += 1
    return count


def count_both_dirs(line):
    if type(line) != str:
        line = ''.join(line)
    return count_in_line(line) + count_in_line(line[::-1])


def get_diagonal(lines, row, col, size, dir=1):
    diag = []
    while row < size and row >= 0 and col < size:
        diag.append(lines[row][col])
        row += 1 * dir
        col += 1
    return diag


with open('input/day-4.txt') as f:
    lines = f.read().split('\n')
    size = len(lines)
    count = sum(count_both_dirs(line) for line in lines)
    count += sum(count_both_dirs([line[i] for line in lines])
                 for i in range(size))

    left_top_diags = [get_diagonal(lines, 0, i, size) for i in range(size)]
    left_side_diags = [get_diagonal(lines, i, 0, size) for i in range(1, size)]
    right_top_diags = [get_diagonal(lines, i, 0, size, -1)
                       for i in range(size)]
    right_side_diags = [get_diagonal(lines, size - 1, i, size, -1)
                        for i in range(1, size)]
    diags = [*left_top_diags, *left_side_diags,
             *right_top_diags, *right_side_diags]
    count += sum(count_both_dirs(diag) for diag in diags)

    print(count)
