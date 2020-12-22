import numpy as np

def returnIfExists(row, chair):
    if row < 0 or chair < 0:
        return None
    try:
        return chairs[row][chair]
    except IndexError:
        return None

def findL(row, chair, offset):
    count = 0
    match = returnIfExists(row, chair - offset)
    if match == '#':
        count += 1
    elif match == '.':
        count += findL(row, chair, offset + 1)
    return count

def findR(row, chair, offset):
    count = 0
    match = returnIfExists(row, chair + offset)
    if match == '#':
        count += 1
    elif match == '.':
        count += findR(row, chair, offset + 1)
    return count

def findU(row, chair, offset):
    count = 0
    match = returnIfExists(row + offset, chair)
    if match == '#':
        count += 1
    elif match == '.':
        count += findU(row, chair, offset + 1)
    return count

def findD(row, chair, offset):
    count = 0
    match = returnIfExists(row - offset, chair)
    if match == '#':
        count += 1
    elif match == '.':
        count += findD(row, chair, offset + 1)
    return count

def findDR(row, chair, offset):
    count = 0
    match = returnIfExists(row - offset, chair + offset)
    if match == '#':
        count += 1
    elif match == '.':
        count += findDR(row, chair, offset + 1)
    return count

def findDL(row, chair, offset):
    count = 0
    match = returnIfExists(row - offset, chair - offset)
    if match == '#':
        count += 1
    elif match == '.':
        count += findDL(row, chair, offset + 1)
    return count

def findUL(row, chair, offset):
    count = 0
    match = returnIfExists(row + offset, chair - offset)
    if match == '#':
        count += 1
    elif match == '.':
        count += findUL(row, chair, offset + 1)
    return count

def findUR(row, chair, offset):
    count = 0
    match = returnIfExists(row + offset, chair + offset)
    if match == '#':
        count += 1
    elif match == '.':
        count += findUR(row, chair, offset + 1)
    return count

def ObtainNewConfiguration():
    newchairs = np.empty((numberofRows, seatsinrow), str)
    for i in range(numberofRows):
        for j in range(seatsinrow):
            neighborsOccupied = 0
            neighborsOccupied += findU(i,j,1)
            neighborsOccupied += findD(i,j,1)
            neighborsOccupied += findL(i,j,1)
            neighborsOccupied += findR(i,j,1)
            neighborsOccupied += findUR(i,j,1)
            neighborsOccupied += findUL(i,j,1)
            neighborsOccupied += findDL(i,j,1)
            neighborsOccupied += findDR(i,j,1)
            if chairs[i][j] == 'L' and neighborsOccupied == 0:
                newchairs[i][j] = '#'
            elif chairs[i][j] == '#' and neighborsOccupied > 4:
                newchairs[i][j] = 'L'
            else:
                newchairs[i][j] = chairs[i][j]
    return newchairs

filldata = []
for line in open('input.txt'):
    filldata.append(line.rstrip())
chairs = np.array(filldata)

seatsinrow = len(chairs[0])
numberofRows=len(chairs)

print(chairs)
while np.array_equal(chairs, ObtainNewConfiguration()) == False:
    chairs = ObtainNewConfiguration()

finalconfig = ObtainNewConfiguration()
count = 0
for i in range(numberofRows):
    for j in range(seatsinrow):
        if finalconfig[i][j] == '#':
            count += 1
print(count)