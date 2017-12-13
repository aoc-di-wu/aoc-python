input = {}
size = 0
with open('inputs/day13.input','r') as f:
    for line in f:
        line = line.strip().split(": ")
        input[int(line[0])] = int(line[1])
        size = int(line[0]) + 1

depths = []
for x in range(size):
    if(x not in input):
        input[x] = 0
    depths.append(input[x])

delay = 0
while True:
    for x in range(size):
        if(depths[x] == 0):
            continue
        if((x + delay) % (depths[x]*2 - 2) == 0):
            break
    else:
        break
    delay += 1

print("Part two: %d" % delay)
