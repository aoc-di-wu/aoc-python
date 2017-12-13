input = {}
with open('inputs/day13.input','r') as f:
    for line in f:
        line = line.strip().split(": ")
        input[int(line[0])] = int(line[1])

size = 99
severity = 0
firewall = []
for x in range(size):
    firewall.append([])
    if(x not in input):
        input[x] = 0
        firewall[x].append(0)
    for y in range(input[x]):
        if(y == 0):
            firewall[x].append(1)
        else:
            firewall[x].append(0)

current = 0
while(current < size):
    if(firewall[current][0] == 1 or firewall[current][0] == -1):
        severity += current*len(firewall[current])

    for x in range(size):
        changed = False
        for y in range(len(firewall[x])):
            if((firewall[x][y] == 1 or firewall[x][y] == -1) and not changed):
                if(firewall[x][y] == 1):
                    if(y + 1 < len(firewall[x])):
                        firewall[x][y + 1] = 1
                    else:
                        firewall[x][y - 1] = -1
                else:
                    if(y - 1 >= 0):
                        firewall[x][y - 1] = -1
                    else:
                        firewall[x][y + 1] = 1
                firewall[x][y] = 0
                changed = True
    current += 1

print("Part one: %d" % severity)
