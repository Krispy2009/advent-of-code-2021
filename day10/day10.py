
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
    from collections import Counter
    invalid_chars = []
    with open('example.txt') as f:
        for line in f.readlines():
            line = line.strip()
            invalid_chars.append(check_line(line))
    invalid_chars = Counter(invalid_chars)
    print(invalid_chars)
if __name__ == "__main__":
    part1()