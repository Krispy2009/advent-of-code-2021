with open("input.txt") as f:
    prev = None
    count = 0
    for line in f.readlines():
        if prev:
            if int(line) > prev:
                count += 1
        prev = int(line)
print(count)
