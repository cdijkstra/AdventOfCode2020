def initializebags(filename):
    rules = [line.rstrip() for line in open(filename)]
    allbags = {}
    for rule in rules:
        bag = '-'.join(rule.split()[0:2])
        contains = rule.split('contain')[1].split(',')
        allbags[bag] = contains
    return allbags

def countallgoldsbags():
    global goldbagcount
    totalgoldbagcount = 0
    for bag in allbags:
        goldbagcount = 0
        countgoldbags(bag)
        if goldbagcount > 0:
            totalgoldbagcount += 1
    return totalgoldbagcount

def countgoldbags(bag):
    global goldbagcount
    for outercontain in allbags[bag]:
        num = outercontain.split()[0]
        if num != 'no':
            innercontain = '-'.join(outercontain.split()[1:3])
            countgoldbags(innercontain)
            if innercontain == 'shiny-gold':
                goldbagcount += 1

def countbagswithinbag(bag, bagcount):
    for outercontain in allbags[bag]:
        num = outercontain.split()[0]
        if num != 'no':
            innerbag = '-'.join(outercontain.split()[1:3])
            bagcount += int(num) * countbagswithinbag(innerbag, 1)
    return bagcount

allbags = initializebags('rules.txt')
print("Total shiny gold bags: " + str(countallgoldsbags()))
print("Bags within shiny gold bag: " + str(countbagswithinbag('shiny-gold', 0)))