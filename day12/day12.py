from collections import defaultdict

path=()
paths=set()

def find_paths_part1(curr_node, destinations, points):
    global path
    path += (curr_node,)            
    if curr_node == 'end':
        paths.add(path)
        print(path)
        path = path[:-1]
        return 
    for node in destinations:
        if node.islower() and path.count(node) == 1:
            continue                   
        else:
            find_paths_part1(node, points[node], points)    
    path = path[:-1]




def part1():
    points = defaultdict(list)
    with open ('input.txt') as f:
        for line in f.readlines():
            node1, node2 = line.strip().split('-')
            points[node1].append(node2)
            points[node2].append(node1)
    find_paths_part1('start', points['start'], points)
    print(f"Part1 ans: {len(paths)}")

def part2():


if __name__ == "__main__":

    part1()
    part2()


