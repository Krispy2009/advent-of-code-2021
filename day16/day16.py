import pdb
import math
from collections import defaultdict

example1 = 'D2FE28'
example2 = '38006F45291200'
example3 = 'EE00D40C823060'
example4 = '8A004A801A8002F478'
example5 = '620080001611562C8802118E34'
example6 = 'C0015000016115A2E0802F182340'
example7 = 'A0016C880162017C3686B18A3D4780'

example8 = 'C200B40A82'
example9 = '04005AC33890'
example10 = '880086C3E88112'
example11 = 'CE00C43D881120'
example12 = 'D8005AC2A8F0'
example13 = 'F600BC2D8F'
example14 = '9C005AC2F8F0'
example15 = '9C0141080250320F1802104A08'

def read_input():
    with open('input.txt') as f:
        for line in f.readlines():
            code = line.strip()
    return code 

inp = read_input()

def decode_hex(hex_num):
    integer = int(hex_num, base=16)
    binary = bin(integer)[2:]
    return(binary)

        

def decode_operator(binary, op_type_id):
    REGISTER = {OPS[op_type_id]: []}
    length_type_id, binary = binary[0], binary[1:]
    if length_type_id == '0':
        # sub_packet_length = 15
        total_length_in_bits = int(binary[:15], base=2)
        binary = binary[15:]
        while total_length_in_bits:
            # print(f"Will read remaining {total_length_in_bits} bits")
            ver, type_id, binary = binary[:3], binary[3:6], binary[6:]
            old_bin_length = len(binary)
            # print(f'packet version: {ver}, type: {type_id}, {binary}')
            VERSIONS.append(ver)

            if type_id == '100':
                binary, val = decode_literals(binary)
                REGISTER[OPS[op_type_id]].append(val)
            else:
                binary,val  = decode_operator(binary, type_id)
                REGISTER[OPS[op_type_id]].append(val)

            total_length_in_bits -= 6
            total_length_in_bits -= (old_bin_length - len(binary))
        
    else:
        # sub_packet_length = 11
        number_of_sub_packets = int(binary[:11], base=2)
        binary = binary[11:]
        while number_of_sub_packets:
            ver, type_id, binary = binary[:3], binary[3:6], binary[6:]
            VERSIONS.append(ver)

            if type_id == '100':
                binary, val = decode_literals(binary)
                REGISTER[OPS[op_type_id]].append(val)

            else:
                binary, val = decode_operator(binary, type_id)
                REGISTER[OPS[op_type_id]].append(val)
            number_of_sub_packets -= 1
          
    return binary, calc_reg(REGISTER)  

def calc_reg(reg):
 
    for i in reg:
        if i == '+':
            return sum(reg[i])
        elif i == '*':
            return math.prod(reg[i])
        if i == 'min':
            return min(reg[i])
        if i == 'max':
            return max(reg[i])
        if i == '>':
            return int(reg[i][0] > reg[i][1])
        if i == '<':
            return int(reg[i][0] < reg[i][1])
        if i == '=':
            return int(reg[i][0] == reg[i][1])

def decode_literals(binary):
    offset = 0
    full_bin = ''
    for i in binary[::5]:
        number = binary[offset:offset+5]
        if len(number) == 5:
            full_bin += number[1:]
            if number[0] == '0':
                # print(f"Found literal {int(full_bin, base=2)}")
                return binary[offset+5:], int(full_bin, base=2)
        offset +=5
    return binary, int(full_bin, base=2)

VERSIONS = []
def part1(hexnum):
    binary = decode_hex(hexnum)
    length = len(binary) + (4 - (len(binary)%4))%4
    binary = binary.zfill(length)

    # import pdb; pdb.set_trace()
    while '1' in binary:
        version, binary = binary[:3], binary[3:]
        type_id, binary = binary[:3], binary[3:]
        
        VERSIONS.append(version)
        if type_id == '100':
            binary, _ = decode_literals(binary)
        else:
            print('Operator')
            binary=decode_operator(binary)
    print('===================================')
    print(f'{VERSIONS} -> {sum([int(i, base=2) for i in VERSIONS])}')
    print('===================================')

OPS = {
    '000' : '+',
    '001' : '*',
    '010' : 'min',
    '011' : 'max',
    '101' : '>',
    '110' : '<',
    '111' : '=',
    '100': 'literal'
    }

def part2(hexnum):
    binary = decode_hex(hexnum)
    length = len(hexnum) * 4
    binary = binary.zfill(length)

    while '1' in binary:
        version, binary = binary[:3], binary[3:]
        type_id, binary = binary[:3], binary[3:]
        # print(f'packet version: {version}, type: {type_id}, {binary}')
        REGISTER = {OPS[type_id]: []}
        VERSIONS.append(version)
        if type_id == '100':
            binary, val = decode_literals(binary)
            REGISTER[OPS[type_id]].append(val)

        else:
            binary, val=decode_operator(binary, type_id)
            REGISTER[OPS[type_id]].append(val)

    print('===================================')
    print(f'{REGISTER}')
    print('===================================')

if __name__ == '__main__':
    # part1(example1)
    # part1(example2)
    # part1(example3)
    # part1(example4)
    # part1(example5)
    # part1(example6)
    # part1(example7)
    # part1(inp)
    
    # part2(example8)
    # part2(example9)
    # part2(example10)
    # part2(example11)
    # part2(example12)
    # part2(example13)
    # part2(example14)
    # part2(example15)
    part2(inp)
