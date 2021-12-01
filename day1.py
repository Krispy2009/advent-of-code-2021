with open("input.txt") as f:
    prev = None
    count = 0
    for line in f.readlines():
        if prev:
            if int(line) > prev:
                count += 1
        prev = int(line)
print(count)

prev = None
count = 0
data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(int(line))
group = [0, 0, 0]
for idx, i in enumerate(data):
    if idx <= len(data) - 3:
        group[0] = i
        group[1] = data[idx + 1]
        group[2] = data[idx + 2]
        if prev and sum(group) > prev:
            # print(group, " = ", sum(group), f" (increase from {prev})")
            count += 1
    prev = sum(group)
print(count)
