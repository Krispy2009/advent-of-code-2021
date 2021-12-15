from pprint import pprint

def find_adj(idx, grid):
    x,y = idx
    adj = set()
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
                adj.add((a,b))
    # print(f"{idx} is adjacent to {adj}")
    return adj

def score_points(points, cave):
    score = 0
    print(points)
    import pdb; pdb.set_trace()
    while points:
        x,y = points.pop()
        score += cave[x][y] + 1
    print(f"Part1: {score}")


with open('input.txt') as f:
    cave = []
    for line in f.readlines():
        cave.append([int(i) for i in line.strip()])
    
    low_points = set()
    for i, row in enumerate(cave):
        for j, height in enumerate(row):
            if height ==9:
                continue
            if height == 0:
                low_points.add((i,j))
            adj = find_adj((i,j), cave)
            for (x,y) in adj:
                if height > cave[x][y]:
                    height = cave[x][y]
                    adj.union(find_adj((x,y), cave))
                else:
                    adj = adj - set([(x,y)])
                    if len(adj) == 0:
                        low_points.add((i,j))

    score_points(low_points, cave)
            


