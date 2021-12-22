import pdb; 
import math
example = [[1,1], [2,2], [3,3], [4,4]]
homework = []
def part1():
    with open('input.txt') as f: 
        for line in f.readlines():
            homework.append(eval(line.strip()))
    print (len(homework)) 
    sn = SnailfishNumber(homework[0], 0, None)
    for line in homework[1:]:
        new_sn = SnailfishNumber(line, 0, None)
        print(f"  {sn}")
        print(f"+ {new_sn}")
        sn = add(sn, new_sn)
        print(f"= {sn}")
        print()

    print(f"Magnitude: {magnitude(sn)}")



class Node():

    def __truediv__(self, a):
        self.value = self.value / a
        return self

    def __ge__(self, a):
        return self.value >= a

    def __add__(self, a):
        self.value = self.value + a.value
        return self

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


    def __init__(self, value, depth,  parent):
        self.value = value
        self.parent = parent
        self.right = None
        self.left = None
        self.depth = depth

    def increase_depth(self):
        self.depth +=1

    def should_split(self):
        return self.value >=10 
    
    def split(self):
        l = math.floor(self.value/2)
        r = math.ceil(self.value/2)

        l = Node(l, self.parent.depth+1, self.parent)
        r = Node(r, self.parent.depth+1, self.parent)

        return SnailfishNumber([l, r], self.depth, self)

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
        elif isinstance(pair[0], (int)):
            self.left = Node(pair[0],self.depth+1, self)
        elif isinstance(pair[0], (Node)):
            self.left = pair[0]
            self.left.depth = self.depth +1
            self.left.parent = self
        if isinstance(pair[1], (list, SnailfishNumber)):
            self.right = SnailfishNumber(pair[1], self.depth+1, self)
        elif isinstance(pair[1], (Node)):
            self.right = pair[1]
            self.right.depth = self.depth +1
            self.right.parent = self
        elif isinstance(pair[1], (int)):
            self.right = Node(pair[1], self.depth+1,self)
    
    def increase_depth(self):
        self.depth += 1
        if isinstance(self, (SnailfishNumber, Node)):
            self.left.increase_depth()
            self.right.increase_depth()
        
    


    def explode(self):
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
                parent.left = Node(0, parent.depth + 1, parent)
            elif parent.right == node:
                parent.right = Node(0, parent.depth + 1, parent)
        

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
                print('After explode: ', self)
                continue

            node = self.find_node_to_split()
            if node and node.should_split():
                new_node = node.split()
                new_node.parent = node.parent

                if node.parent.left == node:

                    node.parent.left = new_node
                else:
                    node.parent.right = new_node
                
                print('After split: ', self)

                continue
            if not self.should_explode() and not self.should_split():
                break
        return self


    def find_node_to_explode(self):
        l, r = None, None
        if self.depth >= 4:
            return self

        if not isinstance(self.left, (int, Node)):
             l = self.left.find_node_to_explode()

        if not isinstance(self.right, (int, Node)):
             r = self.right.find_node_to_explode()

        return l or r
            

    def find_node_to_split(self):
        l, r = None, None
        if isinstance(self.left, Node) and self.left.value >=10:
            l = self.left
        elif isinstance(self.left, SnailfishNumber):
            l = self.left.find_node_to_split()

        if isinstance(self.right, Node) and self.right.value >=10:
            r =  self.right
        elif isinstance(self.right, SnailfishNumber):
            r =  self.right.find_node_to_split()
        
        return l or r



    def should_split(self):
        if isinstance(self.left, Node) and self.left.value >=10:
            return True
        if isinstance(self.right, Node) and self.right.value >=10:
            return True
        else:
            return False

    
def magnitude(n):
    if isinstance(n, Node):
        return n.value
    else:
        return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


def add(num1, num2):
    new_num = SnailfishNumber([num1, num2], -1, None)
    
    num1.parent = new_num
    num2.parent = new_num

    new_num.increase_depth()

    new_num.reduce()

    return new_num

if __name__ == "__main__":
    part1()