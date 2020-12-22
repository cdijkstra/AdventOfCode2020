def loop(preamble):
    offset = 0
    print(f'hmmm {preamble} and {offset}')
    while preamble + offset <= len(int_list):
        for possibleindex in range(offset, preamble + offset - 1):
            if any(int_list[possibleindex] + int_list[possibleindex2] == int_list[preamble + offset] for possibleindex2 in range(possibleindex + 1, preamble + offset)):
                offset += 1
            else:
                if possibleindex == preamble + offset - 2:
                    print(f'Cannot construct {int_list[preamble + offset]}')
                    return


int_list = [int(line) for line in open('ints.txt')]
preamble = 25
loop(preamble)

def sumnumbers():
    index1 = index2 = sum = 0
    while True:
        sum += int_list[index2]
        index2 += 1
        if (sum == number):
            minnum = min(int_list[i] for i in range(index1, index2))
            maxnum = max(int_list[i] for i in range(index1, index2))
            minplusmax = minnum + maxnum
            print(f'Min + max = {minplusmax}')
            return
        elif (sum > number):
            sum = 0
            index1 += 1 # Start with new loop
            index2 = index1

number = 127
number = 14144619
sumnumbers()