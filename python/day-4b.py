def is_x_mas_cross(lines, row, col):
    if lines[row][col] != 'A':
        return 0

    if lines[row - 1][col - 1] == 'M':
        if lines[row + 1][col + 1] != 'S':
            return 0
    elif lines[row - 1][col - 1] == 'S':
        if lines[row + 1][col + 1] != 'M':
            return 0
    else:
        return 0

    if lines[row - 1][col + 1] == 'M':
        if lines[row + 1][col - 1] != 'S':
            return 0
    elif lines[row - 1][col + 1] == 'S':
        if lines[row + 1][col - 1] != 'M':
            return 0
    else:
        return 0

    return 1


with open('input/day-4.txt') as f:
    lines = f.read().split('\n')
    size = len(lines)
    print(sum(is_x_mas_cross(lines, row, col)
              for row in range(1, size - 1) for col in range(1, size - 1)))
