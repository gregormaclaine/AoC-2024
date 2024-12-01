with open('input/day-1.txt') as f:
    data = [line.split('   ') for line in f.read().strip().split('\n')]
    list1 = sorted([int(x[0]) for x in data])
    list2 = sorted([int(x[1]) for x in data])
    print(sum(abs(x - y) for x, y in zip(list1, list2)))
