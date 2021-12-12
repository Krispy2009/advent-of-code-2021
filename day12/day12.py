from collections import defaultdict

path=()
paths=set()
points = defaultdict(list)

def find_paths_part1(curr_node, destinations, points):
    global path
    path += (curr_node,)            
    if curr_node == 'end':
        paths.add(path)
        path = path[:-1]
        return 
    for node in destinations:
        if node.islower() and path.count(node) == 1:
            continue                   
        else:
            find_paths_part1(node, points[node], points)    
    path = path[:-1]




def part1():
    with open ('input.txt') as f:
        for line in f.readlines():
            node1, node2 = line.strip().split('-')
            points[node1].append(node2)
            points[node2].append(node1)
    find_paths_part1('start', points['start'], points)
    print(f"Part1 ans: {len(paths)}")


def find_paths_part2(curr_node, destinations, points, can_visit_twice):
    global path
    path += (curr_node,) 
    if curr_node == 'end':
        paths.add(path)
        path = path[:-1]
        return 
    for node in destinations:
        if node.islower() and node != can_visit_twice and path.count(node) == 1:
            continue        
        if node == can_visit_twice and path.count(node) == 2:  
            continue
        find_paths_part2(node, points[node], points, can_visit_twice)    
    path = path[:-1]

def part2():
    for point in points:
        if point.islower() and point not in ['start', 'end']:
            find_paths_part2('start', points['start'], points, can_visit_twice=point)
    print(f"Part2 ans: {len(paths)}")


if __name__ == "__main__":
    part1()
    part2()


