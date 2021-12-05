from collections import defaultdict

plot_counts = defaultdict(int)


def get_coords(start, end):
    x_step = 1 if start[0] < end[0] else -1
    y_step = 1 if start[1] < end[1] else -1
    for x in range(start[0], end[0] + x_step, x_step):

        for y in range(start[1], end[1] + y_step, y_step):
            plot_counts[(x, y)] += 1


def part1(start, end):
    if start[0] == end[0]:
        print(f"vertical {start} -> {end}")
        get_coords(start, end)
    elif start[1] == end[1]:
        print(f"horizontal {start} -> {end}")
        get_coords(start, end)


with open("input.txt") as f:
    ans = 0
    for line in f.readlines():
        line = line.strip()
        start, end = line.split(" -> ")
        start = tuple([int(i) for i in start.split(",")])
        end = tuple([int(i) for i in end.split(",")])
        part1(start, end)

    for coord, value in plot_counts.items():
        if value > 1:
            ans += 1
    print(f"Part 1 ANS: {ans}")

