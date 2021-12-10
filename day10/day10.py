
def check_line(line):
    open_chars = ['{','[','(', '<']
    bracket_pairs= {'{': '}', '[':']','(':')', '<':'>'}
    matching_pairs = []
    for ch in line:
        if ch in open_chars:
            matching_pairs.append(ch)

        else:
            if ch != bracket_pairs[matching_pairs.pop()]:
                return ch

    
    

def part1():
    scores = {'}':1197,']':57,')':3, '>':25137}
    total_score = 0
    from collections import Counter
    invalid_chars = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            char = check_line(line)
            if char:
                invalid_chars.append(char)
    invalid_chars = Counter(invalid_chars)
    print(invalid_chars)
    for c in invalid_chars:
        total_score += invalid_chars[c] * scores[c]
    
    print(total_score)

def complete_line(line):
    open_chars = ['{','[','(', '<']
    bracket_pairs= {'{': '}', '[':']','(':')', '<':'>'}
    matching_pairs = []

    for ch in line:
        if ch in open_chars:
            matching_pairs.append(ch)

        else:
            if ch == bracket_pairs[matching_pairs.pop()]:
                continue
    return ''.join([bracket_pairs[c] for c in matching_pairs[::-1]])

def score_line(ending):
    total_score = 0
    scores = {'}':3,']':2,')':1, '>':4}
    for c in ending:
        total_score *= 5
        total_score += scores[c]
    return total_score



def part2():
    all_scores = []
    valid_lines = []
    with open('input.txt') as f:
        for line in f.readlines():
            total_score = 0
            line = line.strip()
            char = check_line(line)
            if char is None:
                valid_lines.append(line)
                print(f'{line} is valid')
                ending = complete_line(line)
                print(f'{line} complete by adding {ending}')
                all_scores.append(score_line(ending))
    # for c in invalid_chars:
    #     total_score += invalid_chars[c] * scores[c]
    print(sorted(all_scores)[int(len(all_scores)/2)])
if __name__ == "__main__":
    part2()