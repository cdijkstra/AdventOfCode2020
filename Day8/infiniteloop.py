visitedlines = []

def quitWhenRepeat(linenr):
    global accumulator

    if linenr not in visitedlines:
        visitedlines.append(linenr)
    else:
        print("Accumulator when loop repeats = " + str(accumulator))
        accumulator = 0 # Ensure function can be used again
        visitedlines.clear()
        return

    line = lines[linenr]
    command = line.split(' ')[0]
    number = int(line.split(' ')[1])
    if command == 'acc':
        accumulator += number
        newlinenr = linenr + 1
        if newlinenr >= len(lines):
            print("Loop escaped! Accumulator = " + str(accumulator))
            return
        quitWhenRepeat(newlinenr)
    elif command == 'jmp':
        newlinenr = linenr + number
        if newlinenr >= len(lines):
            print("Loop escaped! Accumulator = " + str(accumulator))
            return
        quitWhenRepeat(newlinenr)
    elif command == 'nop':
        newlinenr = linenr + 1
        if newlinenr >= len(lines):
            print("Loop escaped! Accumulator = " + str(accumulator))
            return
        quitWhenRepeat(newlinenr)

def findMutation():
    count = 0
    for i in indicesJmp:
        lines[i] = 'nop ' + lines[i].split(' ')[1]
        quitWhenRepeat(0)
        lines[i] = 'jmp ' + lines[i].split(' ')[1] # Set back
    for i in indicesNop:
        lines[i] = 'jmp ' + lines[i].split(' ')[1]
        quitWhenRepeat(0)
        lines[i] = 'nop ' + lines[i].split(' ')[1] # Set back

lines = [line.rstrip() for line in open('commands.txt')]
accumulator = 0
quitWhenRepeat(0) # Puzzle 1 <-- | --> Puzzle 2

indicesJmp = [i for i, x in enumerate(lines) if x.split(' ')[0] == 'jmp']
indicesNop = [i for i, x in enumerate(lines) if x.split(' ')[0] == 'nop']
findMutation()
