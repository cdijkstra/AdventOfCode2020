import math

bps = [line.rstrip() for line in open('data.txt')]

def findRow(ch, index, range):
    while(index + 1 <= len(ch)):
        if (ch[index] == 'F'):
            return findRow(ch, index + 1, range(min, math.floor((min + max) / 2)))
        else:
            return findRow(ch, index + 1, range(math.ceil((min + max) / 2), max))
    if (min != max):
        print("WARNING")
    return max

def findColumn(ch, index, range):
    while(index + 1 <= len(ch)):
        if (ch[index] == 'L'):
            return findColumn(ch, index + 1, range(min, math.floor((min + max) / 2)))
        else:
            return findColumn(ch, index + 1, range(math.ceil((min + max) / 2), max))
    if (min != max):
        print("WARNING")
    return max

def seatId(row, column):
    print(row * 8 + column)

# for bp in bps:
bp = "FBFBBFFRLR"
row = findRow(bp[:7], 0, 0, 127)
column = findColumn(bp[-3:], 0, 0, 7)
id = seatId(row, column)