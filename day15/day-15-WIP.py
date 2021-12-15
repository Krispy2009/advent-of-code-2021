from collections import defaultdict
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
                adj.append((a,b))
    # print(f"{idx} is adjacent to {adj}")
    return adj

def find_shortest_path(start, end, graph):
    queue = []

    for n in graph:
        queue.append(n)
        queue += [x[0] for x in graph[n]]
    q = set(queue)
    nodes = list(q)
    dist = dict()
    prev = dict()
    for n in nodes:
        dist[n] = float('inf')
        prev[n] = None

    dist[start] = 0

    while q:
        u = min(q, key=dist.get)
        q.remove(u)

        if u == end:
            return dist[end], prev

        for v, w in graph.get(u, ()):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev

def find_path(pr, node):  # generate path list based on parent points 'prev'
    p = []
    while node is not None:
        p.append(node)
        node = pr[node]
    return p[::-1]

def calc_score(path, grid):
    score = 0
    for (x,y) in path:
        if (x,y) != (0,0):
            score += grid[x][y]
    print(score)

def build_graph(adj, grid):
    graph = defaultdict(list)
    seen_edges = defaultdict(int)
    for src, destinations in adj.items():
        for dest in destinations:
            x,y = dest
            weight = grid[x][y]
            seen_edges[(src, dest, weight)] += 1
            if seen_edges[(src, dest, weight)] > 1:  # checking for duplicated edge entries
                continue
            graph[src].append((dest, weight))
            graph[dest].append((src, weight))  # remove this line of edge list is directed
    return graph



def part1():
    grid = []
    adjacency = {}
    with open('example.txt') as f:
        for line in f.readlines():
            row = [int(i) for i in line.strip()]
            grid.append(row)
        pprint(grid)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                adjacency[(x,y)] = find_adj((x,y), grid)

        graph = build_graph(adjacency, grid)

        print("--- Single source, single destination ---")
        d, prev = find_shortest_path((0,0), (9, 9), graph)
        path = find_path(prev, (9,9))
        print("A -> E: distance = {}, path = {}".format(d, path))
        calc_score(path, grid)
    
if __name__ == '__main__':
    part1()