input = []
with open('inputs/day11.input','r') as f:
    for line in f:
        for word in line.split(','):
            input.append(word)

xCoord = 0
yCoord = 0

steps = 0

for i in input:
    if(len(i) == 1):
        if(i == "n"):
            xCoord += 1
            yCoord -= 1
        elif(i == "s"):
            xCoord -= 1
            yCoord += 1
    else:
        if(i == "ne"):
            xCoord += 1
        elif(i == "se"):
            yCoord += 1
        elif(i == "sw"):
            xCoord -= 1
        elif(i == "nw"):
            yCoord -= 1

    if(abs(xCoord) > steps):
        steps = abs(xCoord)
    elif(abs(yCoord) > steps):
        steps = abs(yCoord)

if(abs(xCoord) > abs(yCoord)):
    solution = abs(xCoord)
else:
    solution = abs(yCoord)

print("Part one: %d" % solution)
print("Part two: %d" % steps)
