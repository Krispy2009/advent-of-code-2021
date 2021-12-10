
def check_line(line):
    open_chars = ['{','[','(', '<']
    closed_chars = ['}',']',')', '>']
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
if __name__ == "__main__":
    part1()