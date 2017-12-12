input = []
with open('inputs/day12.input','r') as f:
    for line in f:
        lines = []
        for word in line.split():
            lines.append(word.strip(','))
        input.append(lines)

def connect(index):
    global group
    a = []
    for x in input[index][2:]:
        a.append(int(x))
    for i in a:
        if(i not in group):
            group += [i]
            connect(i)

connections = []
for y in range(len(input)):
    connections.append(-1)

for i in range(len(input)):
    if(connections[i] == -1):
        group = [i]
        connect(i)
        for j in group:
            connections[j] = i

print("Part one: %d" % connections.count(0))
print('Part two: %d' % len(set(connections)))
