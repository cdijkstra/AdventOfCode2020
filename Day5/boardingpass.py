import math

bps = [line.rstrip() for line in open('data.txt')]

def findRow(ch, index, min, max):
    while(index + 1 <= len(ch)):
        if (ch[index] == 'F'):
            return findRow(ch, index + 1, min, math.floor((min + max) / 2))
        else:
            return findRow(ch, index + 1, math.ceil((min + max) / 2), max)
    return max

def findColumn(ch, index, min, max):
    while(index + 1 <= len(ch)):
        if (ch[index] == 'L'):
            return findColumn(ch, index + 1, min, math.floor((min + max) / 2))
        else:
            return findColumn(ch, index + 1, math.ceil((min + max) / 2), max)
    return max

def seatId(row, column):
    return row * 8 + column

def find_missing(lst): 
    return [x for x in range(min(lst), max(lst)) if x not in lst] 

ids = []
for bp in bps:
    row = findRow(bp[:7], 0, 0, 127)
    column = findColumn(bp[-3:], 0, 0, 7)
    ids.append(seatId(row, column))

print("Max number: " + str(max(ids)))
print("Missing number: " + str(find_missing(ids)))