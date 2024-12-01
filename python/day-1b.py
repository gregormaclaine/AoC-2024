with open('input/day-1.txt') as f:
    data = [line.split('   ') for line in f.read().strip().split('\n')]
    list1 = [int(x[0]) for x in data]
    list2 = [int(x[1]) for x in data]
    print(sum(x * list2.count(x) for x in list1))
