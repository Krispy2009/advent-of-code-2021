import time
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
    output = []
    total = 0
    # example = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    with open('input.txt') as f:
        for line in f.readlines():
            digits = {}
            numbers = {}
            patterns, output = line.split(' | ')
            while len(digits) != 10:
                for o in patterns.split():
                    o = ''.join(sorted(o))
                    if digits.get(o) is not None:
                        continue
                    if len(o) == 2:
                        digits[o] = 1
                        numbers[1] = o
                    elif len(o) == 3:
                        digits[o] = 7
                        numbers[7] = o
                    elif len(o) == 4:
                        digits[o] = 4
                        numbers[4] = o
                    elif len(o) == 7:
                        digits[o] = 8
                        numbers[8] = o
                    elif len(o) == 5:
                        if numbers.get(1) is not None:
                            if o.find(numbers[1][0]) != -1 and o.find(numbers[1][1]) != -1:
                                digits[o] = 3
                                numbers[3] = o
                            elif numbers.get(9) is not None:
                                if set(o + numbers[1]) == set(numbers[9]):
                                    digits[o] = 5
                                    numbers[5] = o
                        elif numbers.get(4) is not None:
                            if len(set(o + numbers[4])) == 7:
                                digits[o] = 2
                                numbers[2] = o
                    elif len(o) == 6:
                        if numbers.get(3) is not None and numbers.get(4) is not None:
                            maybe_9 = "".join(sorted(set(numbers[3] + numbers[4])))
                            if o == maybe_9:
                                digits[o] = 9
                                numbers[9] = o
                            else:
                                if numbers.get(1) is not None: 
                                    if len(set(o + numbers[1])) == 7:
                                        digits[o] = 6
                                        numbers[6] = o
                                    else:
                                        digits[o] = 0
                                        numbers[0] = o
                    print(f'{o} is {digits.get(o)}')
            print(digits)
            num_str = ''
            for out in output.split():
                out = ''.join(sorted(out))
                num_str += str(digits[out])
            total += int(num_str)
            print(f"{output} translates to {num_str}")
            print(f"TOTAL: {total}")
if __name__ == '__main__':
    part2()



                