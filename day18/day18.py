import pdb; 
import math
example = [[1,1], [2,2], [3,3], [4,4]]
homework = []
def part1():
    with open('small-example.txt') as f: 
        for line in f.readlines():
            homework.append(eval(line.strip()))
    print (len(homework)) 
    pdb.set_trace()
    sn = SnailfishNumber(homework[0], 0, None)
    for line in homework[1:]:
        new_sn = SnailfishNumber(line, 0, None)
        print(f"  {sn}")
        print(f"+ {new_sn}")
        sn = add(sn, new_sn)
        print(f"= {sn}")
        print()



class Node():
    def __add__(self, a):
        return self.value + a.value

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        if item == 0:
            return self.left
        if item == 1:
            return self.right
        else:
            print(f'Node attribute says no: {item}')


    def __init__(self, value,depth,  parent):
        self.value = value
        self.parent = parent
        self.right = None
        self.left = None
        self.depth = depth

    def increase_depth(self):
        self.depth +=1
class SnailfishNumber():
    def __repr__(self):
        return self.__str__()


    def __getitem__(self, item):
        if item == 0:
            return self.left
        if item == 1:
            return self.right
        else:
            print(f'attribute says no: {item}')
            

    def __str__(self):
        return f"[{str(self.left)}, {str(self.right)}]"

    def __init__(self, pair, depth, parent):
        self.depth = depth
        self.parent = parent

        if isinstance(pair[0], (list, SnailfishNumber)):
            self.left = SnailfishNumber(pair[0], self.depth+1, self)
        elif isinstance(pair[0], (int, Node)):
            self.left = Node(pair[0],self.depth+1, self)
        if isinstance(pair[1], (list, SnailfishNumber)):
            self.right = SnailfishNumber(pair[1], self.depth+1, self)
        elif isinstance(pair[1], (int,Node)):
            self.right = Node(pair[1], self.depth+1,self)
    
    def increase_depth(self):
        self.depth += 1
        if isinstance(self, (SnailfishNumber, Node)):
            self.left.increase_depth()
            self.right.increase_depth()
        
    


    def explode(self):
        pdb.set_trace()
        leftmost, rightmost = None, None
        node = self.find_node_to_explode()
        
        if node is not None:
            leftmost = node.find_closest_left()
            rightmost = node.find_closest_right()

        if leftmost is not None:
            leftmost += node.left
        if rightmost is not None:
            rightmost += node.right
        
        parent = node.parent
        if parent is not None:
            if parent.left == node:
                parent.left = 0
            elif parent.right == node:
                parent.right = 0
        

    def should_explode(self):
        if self.depth >= 4:
            return True
        return False

    
    def find_closest_left(self):
        if self.parent is None: 
            return None

        if self == self.parent.left:
            return self.parent.find_closest_left()

        node = self.parent.left
        while isinstance(node, SnailfishNumber) and node.right is not None:
            node = node.right
        return node

    def find_closest_right(self):
        pdb.set_trace()
        if self.parent is None: 
            return None
        if self == self.parent.right:
            return self.parent.find_closest_right()

        node = self.parent.right
        while isinstance(node, SnailfishNumber) and node.left is not None:
            node = node.left
        return node
    
    def reduce(self):
        while True:
            node = self.find_node_to_explode()
            if node and node.should_explode():
                node.explode()
                continue

            node = self.find_node_to_split()

            if node and node.should_split():
                node.split()
                continue
            if not self.should_explode() and not self.should_split():
                break
        return self


    def find_node_to_explode(self):
        if self.depth >= 4:
            return self

        if not isinstance(self.left, Node):
            return self.left.find_node_to_explode()
        if not isinstance(self.right, Node):
            return self.right.find_node_to_explode()

        return None
            

    def find_node_to_split(self):
        
        if isinstance(self.left, int) and self.left >=10:
            return self
        elif isinstance(self.left, SnailfishNumber):
            return self.left.find_node_to_split()

        if isinstance(self.right, int) and self.right >=10:
            return self
        elif isinstance(self.right, SnailfishNumber):
            return self.right.find_node_to_split()
        
        return None



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


def add(num1, num2):
    new_num = SnailfishNumber([num1, num2], 0, None)
    
    num1.parent = new_num
    num2.parent = new_num

    new_num.increase_depth()

    new_num.reduce()

    return new_num

if __name__ == "__main__":
    part1()