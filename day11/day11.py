from pprint import pprint
flashes = 0
flashed = []
def flash(octopus, grid):
    global flashes
    flashes +=1
    flashed.append(octopus)
    adj = find_adj(octopus, grid)
    for (x,y) in adj:
        grid[x][y] += 1
        if grid[x][y] == 10:
            flashes += 1
            flashed.append((x,y))
            new_adj = find_adj((x,y), grid)
            adj.extend(new_adj)

def part1():
    grid = []
    with open('input.txt') as f: 
        for line in f.readlines():
            row = []
            for octo in line.strip():
                row.append(int(octo))
            grid.append(row)

    for step in range(100):
        # Energy level inc by 1
        for i, row in enumerate(grid):
            for j, o in enumerate(row):
                grid[i][j] += 1

        # Flash octopuses 
        to_flash = []
        for i, row in enumerate(grid):
            for j, o in enumerate(row):
                if grid[i][j] > 9:
                    to_flash.append((i,j))
                    
        for octo in to_flash:
            flash(octo, grid)


                
        # Reset flashed octopuses
        for i, row in enumerate(grid):
            for j, o in enumerate(row):
                if grid[i][j] > 9:
                    grid[i][j] = 0
        if step%10 == 0:
            print(f'After step {step+1}')
        pprint(grid)
        print(flashes)

def find_adj(idx, grid):
    x,y = idx
    adj = []
    for a in range(x-1,x+2):
        if a >= len(grid) or a < 0:
            continue 
        for b in range(y-1, y+2):
            if b >= len(grid[0]) or b < 0:
                continue
            if (a, b) != (x, y):
                adj.append((a,b))
    # print(f"{idx} is adjacent to {adj}")
    return adj
            
   

if __name__ == "__main__":
    part1()