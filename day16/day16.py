example1 = 'D2FE28'
example2 = '8A004A801A8002F478'
example3 = '620080001611562C8802118E34'
example4 = 'C0015000016115A2E0802F182340'
example5 = 'A0016C880162017C3686B18A3D4780'

def read_input():
    with open('input.txt') as f:
        for line in f.readlines():
            code = line.split()
    return code 

input = read_input()

def decode_hex(hex_num):
    integer = int(hex_num, base=16)
    binary = bin(integer)[2:]
    print(binary)
    return(binary)

def part1():
    binary = decode_hex(example1)
    version, binary = binary[:3], binary[3:]
    type_id, binary = binary[:3], binary[3:]
    print(version, type_id, binary)
    if type_id == '100':
        numbers = []
        print(binary)
        offset = 0
        for idx, part in enumerate(binary[::5]):
            print(part)
            numbers.append(binary[offset:offset+5])
            offset +=5
        full_bin = ''

        for n in numbers:

            if len(n) == 5:
                full_bin += n[1:]
        

        print(numbers)
        print(int(full_bin, base=2))



if __name__ == '__main__':
    part1()
