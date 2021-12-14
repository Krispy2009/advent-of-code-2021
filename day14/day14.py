
from collections import Counter
def build_compound(template, instructions):
    new_temp = ''
    for i in range(len(template)-1):
        for inst in instructions:
            if template[i] + template[i+1] == inst:
                new_temp += template[i] + instructions[inst]
    new_temp += template[-1]
    template = new_temp
    return template
        


def part1():
    with open('input.txt') as f:
        template = None
        instructions = {}
        for line in f.readlines():
            if ' -> ' not in line and line != '\n':
                template = line.strip()
            elif line == '\n':
                continue
            else:
                pattern, result = line.strip().split(' -> ')
                instructions[pattern] = result
    for i in range(10):
        print(f'step {i}')
        template = build_compound(template, instructions)
    counts = Counter(template)
    print(counts)
    maximum = max(counts.values())
    minimum = min(counts.values())
    print(f'{maximum} - {minimum}')
    print(f'ANs: {maximum-minimum}')
if __name__ == '__main__':
    part1()