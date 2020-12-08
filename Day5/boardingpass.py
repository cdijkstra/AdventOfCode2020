import math

bps = [line.rstrip() for line in open('data.txt')]

def findRow(ch, index, min, max):
    while(index + 1 <= len(ch)):
        if (ch[index] == 'F'):
            return findRow(ch, index + 1, min, math.floor((min + max) / 2))
        else:
            return findRow(ch, index + 1, math.ceil((min + max) / 2), max)
    if (min != max):
        print("WARNING")
    return max

def findColumn(ch, index, min, max):
    while(index + 1 <= len(ch)):
        if (ch[index] == 'L'):
            return findColumn(ch, index + 1, min, math.floor((min + max) / 2))
        else:
            return findColumn(ch, index + 1, math.ceil((min + max) / 2), max)
    if (min != max):
        print("WARNING")
    return max

def seatId(row, column):
    return row * 8 + column

maxfoundid = 0
for bp in bps:
    row = findRow(bp[:7], 0, 0, 127)
    column = findColumn(bp[-3:], 0, 0, 7)
    id = seatId(row, column)
    if (id > maxfoundid):
        maxfoundid = id

print(maxfoundid)