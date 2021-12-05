from collections import defaultdict

plot_counts = defaultdict(int)


# def test_get_coords():
#     plot_counts.clear()
#     start = (9, 7)
#     end = (7, 9)
#     get_coords(start, end, diagonal=True)
#     print(plot_counts)


def get_coords(start, end, diagonal=False):
    x_step = 1 if start[0] < end[0] else -1
    y_step = 1 if start[1] < end[1] else -1
    if not diagonal:
        for x in range(start[0], end[0] + x_step, x_step):
            for y in range(start[1], end[1] + y_step, y_step):
                plot_counts[(x, y)] += 1
    else:
        y = start[1]
        for x in range(start[0], end[0] + x_step, x_step):
            plot_counts[(x, y)] += 1
            y += y_step


def part1(start, end):
    if start[0] == end[0]:
        print(f"vertical {start} -> {end}")
        get_coords(start, end)
    elif start[1] == end[1]:
        print(f"horizontal {start} -> {end}")
        get_coords(start, end)


def part2(start, end):
    diagonal = not (start[0] == end[0] or start[1] == end[1])
    get_coords(start, end, diagonal=diagonal)


with open("input.txt") as f:
    ans = 0
    for line in f.readlines():
        line = line.strip()
        start, end = line.split(" -> ")
        start = tuple([int(i) for i in start.split(",")])
        end = tuple([int(i) for i in end.split(",")])
        # part1(start, end)
        part2(start, end)
    for coord, value in plot_counts.items():
        if value > 1:
            ans += 1
    print(f"Part 2 ANS: {ans}")

# if __name__ == "__main__":
#     test_get_coords()
