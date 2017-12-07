holding = {}
weights = {}
with open('inputs/day07.input','r') as f:
    for line in f:
        count = 0
        hold = set()
        for word in line.split():
            if(count == 0):
                name = word
            elif(count == 1):
                weights[name] = int(word.strip('()'))
            else:
                if(len(word) is not 2):
                    hold.add(word.strip(','))

            count += 1
        if(len(hold) > 0):
            holding[name] = hold

name = ""
for x in holding.keys():
    found = False
    for y in holding.values():
        if x in y:
            found = True
            break

    if not found:
        name = x
        break

print("Part one: %s" % name)
