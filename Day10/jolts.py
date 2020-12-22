from functools import lru_cache 

def calculateproduct():
    difones = difthrees = 0
    for i in range(1, len(jolts)):
        if jolts[i] - jolts[i - 1] == 1:
            difones += 1
        elif jolts[i] - jolts[i - 1] == 3:
            difthrees += 1
    return difones * difthrees

@lru_cache(maxsize = 5)
def countways(leftindex):
    answer = 0
    leftnumber = jolts[leftindex]
    if jolts[-1] - leftnumber < 4:
        return 1

    for rightnumber in jolts[leftindex + 1:leftindex + 4]:
        if rightnumber - leftnumber < 4:
            answer += countways(jolts.index(rightnumber))
    return answer

jolts = [int(line.rstrip()) for line in open('jolts.txt')]
jolts.sort()

jolts.insert(0, 0)          # add 0V to start with
jolts.append(jolts[-1] + 3) # Highest jolt (+3 from last in sorted list)

print(f'Ones times threes = {calculateproduct()}')
print(f'Total amount of possibilities = {countways(0)}')
