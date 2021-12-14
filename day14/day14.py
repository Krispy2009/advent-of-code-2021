
from collections import Counter, defaultdict

def build_compound(template, instructions):
    new_temp = ''
    for i in range(len(template)-1):
        inst = template[i] + template[i+1]
        if inst in instructions:
            new_temp += template[i] + instructions[inst]
    new_temp += template[-1]
    template = new_temp
    return template

total_counts = defaultdict(int)
def build_compound_dicts(template_dict, instructions):
    new_dict = defaultdict(int)
    for s in template_dict:
        if s in instructions:
            char_to_add = instructions[s]
            first_half = s[0] + char_to_add
            sec_half = char_to_add + s[1]
            new_dict[first_half] += template_dict[s]
            new_dict[sec_half] += template_dict[s]

        total_counts[char_to_add] += template_dict[s]
    return new_dict


def part1():
    with open('example.txt') as f:
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


def part2():
    with open('input.txt') as f:
        instructions = {}
        template_dict = defaultdict(int)
        for line in f.readlines():
            if ' -> ' not in line and line != '\n':
                template = line.strip()
                for i in range(len(template)-1):
                    template_dict[template[i]+template[i+1]] += 1 
                    total_counts[template[i]] += 1
                total_counts[template[len(template)-1]] += 1
            elif line == '\n':
                continue
            else:
                pattern, result = line.strip().split(' -> ')
                instructions[pattern] = result
    for i in range(40):
        print(f'step {i}')
        template_dict = build_compound_dicts(template_dict, instructions)

    print(total_counts)
    maximum = max(total_counts.values())
    minimum = min(total_counts.values())
    print(f'{maximum} - {minimum}')
    print(f'ANs: {maximum-minimum}')

if __name__ == '__main__':
    part2()