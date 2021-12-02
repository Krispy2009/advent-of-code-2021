horizontal, depth = 0, 0
with open("input.txt") as f:
    for line in f.readlines():
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance

    print(f"horizontal: {horizontal} x depth: {depth} = {horizontal*depth}")

horizontal, depth, aim = 0, 0, 0
with open("input.txt") as f:
    for line in f.readlines():
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    print(f"horizontal: {horizontal} x depth: {depth} = {horizontal*depth}")
