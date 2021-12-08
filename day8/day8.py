def part1():
    count = 0
    with open('input.txt') as f:
        for line in f.readlines():
            _, out = line.split(' | ')
            for o in out.split():
                if len(o) in [2, 3, 4, 7]:
                    count += 1
    print(count)

def part2():
    digits = {}
    numbers = {}
    output = []
    with open('input.txt') as f:
        for line in f.readlines():
            _, out = line.split(' | ')
            output.push(out) 
            for o in out.split():
                o = sorted(o)
                if digits.get(o) is None:
                    if len(o) == 2:
                        digits[o] = 1
                        numbers[2] = o
                    elif len(o) == 3:
                        digits[o] = 7
                        numbers[7] = o
                    elif len(o) == 4:
                        digits[o] = 4
                        numbers[4] = o
                    elif len(o) == 7:
                        digits[o] = 8
                        numbers[8] = o
                    elif len(o) == 5 and o.index(numbers[1]) != -1:
                        digits[o] = 3
                        numbers[3] = o


                