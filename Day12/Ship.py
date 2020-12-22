import math

instruction = [line.rstrip() for line in open('input.txt')]

x = 0
y = 0

direction = {
    0: 'N',
    1: 'E',
    2: 'S',
    3: 'W'
}
val_list = list(direction.values())

dir = direction[1]

for ins in instruction:
    print(ins)
    letter = ins[0]
    num = int(ins[1:])

    if letter == 'F':
        if dir == 'N':
            y += num
        if dir == 'E':
            x += num
        if dir == 'S':
            y -= num
        if dir == 'W':
            x -= num
    elif letter == 'N':
        y += num
    elif letter == 'E':
        x += num
    elif letter == 'S':
        y -= num
    elif letter == 'W':
        x -= num
    elif letter == 'L':
        if num == 90:
            newindex = (int(val_list.index(dir)) - 1) % 4
            dir = direction[newindex]
        elif num == 180:
            newindex = (int(val_list.index(dir)) - 2) % 4
            dir = direction[newindex]
        elif num == 270:
            newindex = (int(val_list.index(dir)) - 3) % 4
            dir = direction[newindex]
    elif letter == 'R':
        if num == 90:
            newindex = (int(val_list.index(dir)) + 1) % 4
            dir = direction[newindex]
        elif num == 180:
            newindex = (int(val_list.index(dir)) + 2) % 4
            dir = direction[newindex]
        elif num == 270:
            newindex = (int(val_list.index(dir)) + 3) % 4
            dir = direction[newindex]
    else:
        print('whuuut')

distance = abs(x) + abs(y)
print(f'Location (x,y) is ({x},{y})')
print(f'Distance is {distance}')