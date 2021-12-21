import pdb; 
import math
example = [[1,1], [2,2], [3,3], [4,4]]
homework = []
def part1():
    with open('example.txt') as f: 
        for line in f.readlines():
            homework.append(eval(line.strip()))
    print (len(homework)) 
    sn = SnailfishNumber(homework[0], 0, None)
    pdb.set_trace()
    for line in homework[1:]:
        new_sn = SnailfishNumber(line, 0, None)
        sn = sn.addition(new_sn)
        print(sn)



class SnailfishNumber():
    def __str__(self):
        print(f"<{self.left}, {self.right}>")
    def __init__(self, pair, depth, parent):
        self.depth = depth
        self.parent = parent

        if isinstance(pair[0], list):
            self.left = SnailfishNumber(pair[0], self.depth+1, self)
        if isinstance(pair[0], SnailfishNumber):
            self.left = SnailfishNumber(pair.left, self.depth+1, self)
        elif isinstance(pair[0], int):
            self.left = int(pair[0])
        if isinstance(pair[1], list):
            self.right = SnailfishNumber(pair[1], self.depth+1, self)
        if isinstance(pair[1], SnailfishNumber):
            self.right = SnailfishNumber(pair.right, self.depth+1, self)
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

        new_num.reduce()

        return new_num

    def should_explode(self):
        if self.depth >= 4:
            return True

    def explode(self):
        left = self.left
        right = self.right

        leftmost = left.find_leftmost()
        rightmost = right.find_rightmost()

        if leftmost is not None:
            leftmost.left += left
        if rightmost is not None:
            rightmost.right += right
        
        parent = self.parent
        if parent.left == self:
            parent.left = 0
        elif parent.right == self:
            parent.right = 0
        



    def find_leftmost(self):
        if isinstance(self.parent.left, int):
            return self.parent
        elif isinstance(self.parent.left, list) and self.parent is not None:
            return self.parent.left.find_leftmost()
        else:
            return None
        

    def find_rightmost(self):
        if isinstance(self.parent.right, int):
            return self.parent
        else:
            return self.parent.right.find_rightmost()
    
    def reduce(self):
        while True:
            if self.should_explode():
                self.explode()
            elif self.should_split():
                self.split()
            return self

    def should_split(self):
        if isinstance(self.left, int) and self.left >=10:
            return True
        elif isinstance(self.right, int) and self.right >=10:
            return True
        else:
            return False
    
    def split(self):
        if isinstance(self.left, int) and self.left >=10:
            l = math.floor(self.left/2)
            r = math.ceil(self.left/2)
            self.left = SnailfishNumber([l, r], self.depth, self)


if __name__ == "__main__":
    part1()