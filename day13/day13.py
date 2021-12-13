from collections import defaultdict
def print_grid(data):
    biggest_X = max(data, key=lambda x: x[0])[0]
    biggest_Y = max(data, key=lambda x: x[1])[1]
    for y in range(biggest_Y+1):
        for x in range(biggest_X+1):
            if data[(x,y)]:
                print('#', end='')
            else:
                print('.', end='')
        print()

def translate(number, fold_line):
    return abs(fold_line - (number - fold_line))



def fold_h(fold_line, data):
    new_data = defaultdict(lambda: None)
    for item in data:
        if item[1] > fold_line:
            new_item = (item[0], translate(item[1], fold_line))
            new_data[new_item] = 1
        else:
            new_data[item] = data[item]
    return new_data


def fold_v(fold_line, data):
    new_data = defaultdict(lambda: None)
    for item in data:
        if item[0] > fold_line:
            if data[item] == 1:
                new_item = (translate(item[0], fold_line), item[1])
                new_data[new_item] = 1
        else:
            if new_data[item] != 1:
                new_data[item] = data[item]
    return new_data




def part1():
    data = defaultdict(lambda: None)
    instructions = []
    with open('input.txt') as f:
        for line in f.readlines():
            if line == '\n':
                continue
            if line.startswith('fold along'):
                inst= line.replace('fold along ','').strip()
                instructions.append(tuple(inst.split('=')))
                continue
            else:
                line = line.strip().split(',')
                point = tuple([int(i) for i in line])
                data[point] = 1

    for instruction in instructions:

        print(f"Fold along {instruction[0]}={instruction[1]}")
        if instruction[0] == 'y':
            data = fold_h(int(instruction[1]), data)
        if instruction[0] == 'x':
            data = fold_v(int(instruction[1]), data)
        
    print_grid(data)

    # print(sum([1 for o in data.values() if o is not None]))

if __name__ == "__main__":
    part1()