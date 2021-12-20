import pdb; 
example = [[1,1], [2,2], [3,3], [4,4]]
homework = []
def part1():
    with open('example.txt') as f: 
        for line in f.readlines():
            homework.append(eval(line.strip()))
    print (homework) 
    pairs = SnailfishNumber(homework, 0, None)
    pdb.set_trace()

class SnailfishNumber():
    def __init__(self, pair, depth, parent):
        self.depth = depth
        self.parent = parent

        if isinstance(pair[0], list):
            self.left = SnailfishNumber(pair[0], self.depth+1, self)
        elif isinstance(pair[0], int):
            self.left = int(pair[0])
        if isinstance(pair[1], list):
            self.right = SnailfishNumber(pair[1], self.depth+1, self)
        elif isinstance(pair[1], int):
            self.right = int(pair[1])
    
    def increase_depth(self):
        self.depth += 1
        if isinstance(self, list):
            self.left.increase_depth()
            self.right.increase_depth()
        
    
    def addition(self, number):
        new_num = SnailfishNumber([self, number], 0, None)
        new_num.increase_depth()

    def should_explode(node):
        if node.depth == 4:
            return True
if __name__ == "__main__":
    part1()