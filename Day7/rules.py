rules = [line.rstrip() for line in open('rules.txt')]

allbags = {}
for rule in rules:
    bag = '-'.join(rule.split()[0:2])
    contains = rule.split('contain')[1].split(',')
    allbags[bag] = contains

def countgoldbags(bag):
    global goldbagcount
    for outercontain in allbags[bag]:
        num = outercontain.split()[0]
        if num != 'no':
            innercontain = '-'.join(outercontain.split()[1:3])
            if innercontain == 'shiny-gold':
                goldbagcount += 1
            countgoldbags(innercontain)
        else: # No inner bags
            exit

goldbagcount = 0
totalgoldbagcount = 0
for bag in allbags:
    goldbagcount = 0
    countgoldbags(bag)
    if goldbagcount > 0:
        totalgoldbagcount += 1
        
print(totalgoldbagcount)