bits = None
count = 0
with open("input.txt") as f:
    for line in f.readlines():
        count += 1
        if not bits:
            bits = [0] * len(line.strip())
        for idx, bit in enumerate(line.strip()):
            bits[idx] += int(bit)
        print(bits)
    gamma_bits = []
    for idx, bit in enumerate(bits):
        print(bits[idx], count / 2)
        gamma_bits.append(int(bits[idx] > count / 2))
        print(gamma_bits)
        epsilon_bits = [int(not g) for g in gamma_bits]
        print(epsilon_bits)
    gamma = int("".join([str(g) for g in gamma_bits]), 2)
    epsilon = int("".join(str(e) for e in epsilon_bits), 2)

    print(gamma * epsilon)

