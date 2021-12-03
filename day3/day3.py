import pdb


def calculate_g_and_e(lines):
    count = 0
    bits = None
    for line in lines:
        count += 1
        if not bits:
            bits = [0] * len(line.strip())
        for idx, bit in enumerate(line.strip()):
            bits[idx] += int(bit)
        print(bits)
    gamma_bits = []
    for idx, bit in enumerate(bits):
        gamma_bits.append(int(bit >= count / 2))
        epsilon_bits = [int(not g) for g in gamma_bits]
    return gamma_bits, epsilon_bits


def part1():
    with open("input.txt") as f:
        gamma_bits, epsilon_bits = calculate_g_and_e(f.readlines)
        gamma = int("".join([str(g) for g in gamma_bits]), 2)
        epsilon = int("".join(str(e) for e in epsilon_bits), 2)

        print(gamma * epsilon)


def part2():
    temp_list = []
    with open("input.txt") as f:
        data = f.readlines()
        gamma_bits, _ = calculate_g_and_e(data)
        for idx, bit in enumerate(gamma_bits):
            for line in data:
                print(f"idx: {idx}, line: {line}, bit to match {bit}, gamma_bits: {gamma_bits}")
                if int(line[idx]) == gamma_bits[idx]:
                    temp_list.append(line.strip())
            print(f"temp_list: {temp_list[:7]}")
            data = temp_list
            if len(data) == 1:
                oxygen = int("".join([str(g) for g in temp_list[0]]), 2)
                print(f"Oxygen generator rating: {oxygen}")

            gamma_bits, _ = calculate_g_and_e(data)
            temp_list = []

    temp_list = []
    with open("input.txt") as f:
        data = f.readlines()
        _, epsilon_bits = calculate_g_and_e(data)
        for idx, bit in enumerate(epsilon_bits):
            for line in data:
                print(f"idx: {idx}, line: {line}, bit to match {bit}, gamma_bits: {gamma_bits}")
                if int(line[idx]) == epsilon_bits[idx]:
                    temp_list.append(line.strip())
            print(f"temp_list: {temp_list[:7]}")
            data = temp_list
            if len(data) == 1:
                co2 = int("".join([str(g) for g in temp_list[0]]), 2)
                print(f"CO2 generator rating: {co2}")
                print(f"ANS: {oxygen*co2}")
                exit()
            _, epsilon_bits = calculate_g_and_e(data)
            temp_list = []


if __name__ == "__main__":
    part2()
