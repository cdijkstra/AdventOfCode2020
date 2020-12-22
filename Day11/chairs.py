import numpy as np

def returnIfNeighbor(row, chair):
    if row < 0 or chair < 0:
        return None
    try:
        return chairs[row][chair]
    except IndexError:
        return None

def ObtainNewConfiguration():
    newchairs = np.empty((numberofRows, seatsinrow), str)
    for i in range(numberofRows):
        for j in range(seatsinrow):
            neighborsOccupied = 0 # Check neighbor seats
            for neighx in range(i - 1, i + 2):
                for neighy in range(j - 1, j + 2):
                    if not (i == neighx and j == neighy):
                        neighbor = returnIfNeighbor(neighx, neighy)
                        if neighbor == '#':
                            neighborsOccupied += 1
            if chairs[i][j] == 'L' and neighborsOccupied == 0:
                newchairs[i][j] = '#'
            elif chairs[i][j] == '#' and neighborsOccupied > 3:
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

# ObtainNewConfiguration()
print(chairs)
while np.array_equal(chairs, ObtainNewConfiguration()) == False:
    chairs = ObtainNewConfiguration()

print('Hurray')
finalconfig = ObtainNewConfiguration()
print(finalconfig)
count = 0
for i in range(numberofRows):
    for j in range(seatsinrow):
        if finalconfig[i][j] == '#':
            count += 1
print(count)