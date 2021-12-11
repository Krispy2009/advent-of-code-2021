from pprint import pprint
with open('example.txt') as f:
    cave = []
    for line in f.readlines():
        cave.append([int(i) for i in line.strip()])

    pprint(cave)
