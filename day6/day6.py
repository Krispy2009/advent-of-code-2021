from collections import Counter
import pdb

#initial_state = [3,4,3,1,2]
initial_state =[1,4,1,1,1,1,1,1,1,4,3,1,1,3,5,1,5,3,2,1,1,2,3,1,1,5,3,1,5,1,1,2,1,2,1,1,3,1,5,1,1,1,3,1,1,1,1,1,1,4,5,3,1,1,1,1,1,1,2,1,1,1,1,4,4,4,1,1,1,1,5,1,2,4,1,1,4,1,2,1,1,1,2,1,5,1,1,1,3,4,1,1,1,3,2,1,1,1,4,1,1,1,5,1,1,4,1,1,2,1,4,1,1,1,3,1,1,1,1,1,3,1,3,1,1,2,1,4,1,1,1,1,3,1,1,1,1,1,1,2,1,3,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,5,1,1,1,2,2,1,1,3,5,1,1,1,1,3,1,3,3,1,1,1,1,3,5,2,1,1,1,1,5,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,5,1,4,3,3,1,3,4,1,1,1,1,1,1,1,1,1,1,4,3,5,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,1,4,4,1,1,1,1,1,1,1,5,1,1,2,5,1,1,4,1,3,1,1]
def part1():
    for day in range(1,81):
        temp = [i  for i in initial_state]
        extra_fish = []
        print(f'Day: {day}')
        for idx, fish in enumerate(initial_state):
            if fish == 0:
                extra_fish.append(8)
                fish = 6
            else:
                fish -= 1
            temp[idx] = fish
        temp.extend(extra_fish)
        initial_state = temp
        # print(f"After {day} day {temp}")
    print(len(temp))

def part2():

    counts = Counter(initial_state)
    for i in range(9):
        if i not in counts:
            counts[i] = 0
    for day in range(1,257):
        count_8 = counts[8]
        count_6 = counts[6]

        # import pdb; pdb.set_trace()
        for item in range(len(counts)):
            if item == 0:
                counts[8] = counts[0]
                counts[6] = counts[0]
            else:
                if item == 6:
                    counts[5] = count_6
                elif item == 8:
                    counts[7] = count_8
                elif item == 7:
                    counts[6] = counts[7] + counts[6]
                else:
                    
                    counts[item-1] = counts[item]
    print(sum([val for k, val in counts.items()]))

if __name__ == "__main__":
    part2()
