def part1():
    count = 0
    with open('input.txt') as f:
        for line in f.readlines():
            _, out = line.split(' | ')
            for o in out.split():
                if len(o) in [2, 3, 4, 7]:
                    count += 1
    print(count)

