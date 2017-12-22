input = []
with open('inputs/day22.input', 'r') as f:
    for line in f:
        l = []
        for c in line.strip('\n'):
            l.append(c)
        input.append(l)

infected = set()
for x in range(len(input[0])):
    for y in range(len(input)):
        if (input[y][x] == '#'):
            infected.add((x, y))

x = len(input[0])//2
y = len(input)//2
v = "u"

count = 0

for _ in range(10000):
    if ((x, y) in infected):
        if (v == "u"): v = "r"
        elif (v == "r"): v = "d"
        elif (v == "d"): v = "l"
        elif (v == "l"): v = "u"
        infected.remove((x, y))
    else:
        if (v == "u"): v = "l"
        elif (v == "r"): v = "u"
        elif (v == "d"): v = "r"
        elif (v == "l"): v = "d"
        infected.add((x, y))
        count += 1

    if(v == "u"): y -= 1
    elif(v == "r"): x += 1
    elif(v == "d"): y += 1
    elif(v == "l"): x -= 1

print("Part one: %d" % count)
