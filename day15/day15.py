from os import getgrouplist
from pprint import pprint
def find_adj(idx, grid):
    x,y = idx
    adj = list()
    for a in range(x-1,x+2):
        if a >= len(grid) or a < 0:
            continue 
        for b in range(y-1, y+2):
            if a != x and b != y:
                continue
            if b >= len(grid[0]) or b < 0:
                continue
            if (a, b) != (x, y):
                cost = grid[a][b]
                adj.append(((a,b), cost))
    # print(f"{idx} is adjacent to {adj}")
    return adj

def find_shortest_path(start, end, graph):
    distance = {node: 999999999 for node in graph}
    distance[start] = 0
    dict_node_length = {start: 0}

    while dict_node_length:
        
        current_source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
        del dict_node_length[current_source_node]

        for node_dist in graph[current_source_node]:
            adjnode = node_dist[0]
            length_to_adjnode = node_dist[1]
            if distance[adjnode] > distance[current_source_node] + length_to_adjnode:
                distance[adjnode] = distance[current_source_node] + length_to_adjnode
                dict_node_length[adjnode] = distance[adjnode]
    
    print(distance[end])


def part1():
    grid = []
    graph = {}
    with open('input.txt') as f:
        for line in f.readlines():
            row = [int(i) for i in line.strip()]
            grid.append(row)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                graph[(x,y)] = find_adj((x,y), grid)
        end = (len(grid)-1, len(grid[0])-1)
        find_shortest_path((0,0), end, graph)

def expand_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for i in range (1,6):
            for item in row:
                new_number = (item+i-1)
                if new_number > 9:
                    new_number = (new_number%10) + 1
                new_row.append(new_number)
        new_grid.append(new_row)
    newer_grid = []

    for i in range(5):
        for row in new_grid:
            newer_row = []
            for item in row:
                new_number = (item+i)
                if new_number > 9:
                    new_number = (new_number%10) + 1
                newer_row.append(new_number)
            newer_grid.append(newer_row)


    return newer_grid




def part2():
    grid = []
    graph = {}
    with open('input.txt') as f:
        for line in f.readlines():
            row = [int(i) for i in line.strip()]
            grid.append(row)

        grid = expand_grid(grid)
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                graph[(x,y)] = find_adj((x,y), grid)

        end = (len(grid)-1, len(grid[0])-1)

        find_shortest_path((0,0), end, graph)

    
if __name__ == '__main__':
    part2()