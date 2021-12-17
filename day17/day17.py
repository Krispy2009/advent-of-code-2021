import pdb
# Example
# x1,x2=20,30
# y1,y2=-10,-5
# Input
x1,x2=25,67
y1,y2=-260,-200

def step(x,y,x_velocity, y_velocity):
    x += x_velocity
    y += y_velocity
    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1
    y_velocity -= 1

    return (x,y,x_velocity, y_velocity)


def shoot_probe(x_vel, y_vel, target_X, target_Y):
    x,y = 0,0
    path = []
    while True:
        x, y, x_vel, y_vel = step(x,y,x_vel, y_vel)
        path.append((x,y))
        if target_X[0] <= x <= target_X[1] and target_Y[1] <= y <= target_Y[0]:
            return path 
        if y < target_Y[1]:
            break



def part1():
    highest_points = []
    for x_vel in range(x2+1):
        for y_vel in range(y2, -y1):
            path = shoot_probe(x_vel, y_vel, (x1,x2), (y2,y1))
            if path:
                highest_point = sorted(path, key=lambda x: x[1], reverse=True)[0][1]
                highest_points.append(highest_point)
    print(f"Part1: {max(highest_points)}")

def part2():
    velocities = []
    for x_vel in range(x2+1):
        for y_vel in range(y1, -y1+1):
            path = shoot_probe(x_vel, y_vel, (x1,x2), (y2,y1))
            if path:
                velocities.append((x_vel, y_vel))
    print(f"Part2: {len(velocities)}")
    

if __name__ == "__main__":
    part1()
    part2()