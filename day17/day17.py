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
            break 
        if y < target_Y[1]:
            break

    for (a,b) in path:
        if target_Y[1] <= b <= target_Y[0] and target_X[0] <= a <= target_X[1]:
            return path



def part1():
    highest_points = {}
    for x_vel in range(x2+1):
        for y_vel in range(y1, -y1+1):
            path = shoot_probe(x_vel, y_vel, (x1,x2), (y2,y1))
            if path:
                highest_point = sorted(path, key=lambda x: x[1], reverse=True)[0][1]
                highest_points[highest_point] = (x_vel, y_vel)
                print(f'found a path to the target with initial vel: {(x_vel, y_vel)} reaching {highest_point}')
                print(max(highest_points))
    return max(highest_points)



# def part1():
#     x,y = 0,0
#     points = []
#     for x_vel in range(-x2, x2):
#         for y_vel in range(y1, -y1):
#             for _ in range(10):
#                 x, y, x_vel, y_vel = step(x,y,x_vel,y_vel)
#                 print((x,y), f'xV {x_vel}, yV {y_vel}') 
#                 points.append((x,y))
#                 if is_after_target(x,y):
#                     print(points)
#                     import pdb; pdb.set_trace()

    

if __name__ == "__main__":
    part1()