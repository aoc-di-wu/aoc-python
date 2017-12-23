input = []
with open('inputs/day23.input','r') as f:
    for line in f:
        l = line.strip('\n')
        c = l.split()
        cmd = []
        for x in c:
            try:
                cmd.append(int(x))
            except ValueError:
                cmd.append(x)
        input.append(cmd)

r = {'a': 0, 'b': 0, 'c': 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

def getValue(v):
    try:
        return int(v)

    except ValueError:
        return r[v]

count = 0
cur = 0

steps = 0
while (0  <= cur < len(input)):
    cmd = input[cur]
    c = cmd[0]

    if (c == "jnz"):
        if (getValue(cmd[1]) != 0):
            cur += getValue(cmd[2])
        else:
            cur += 1
    else:
        if(c == "set"):
            r[cmd[1]] = getValue(cmd[2])

        if(c == "sub"):
            r[cmd[1]] -= getValue(cmd[2])

        if (c == "mul"):
            r[cmd[1]] *= getValue(cmd[2])
            count += 1

        cur += 1

print("Part one: %d" % count)

h = 0

for x in range(107900, 124900 + 1, 17):
    for i in range(2, x):
        if x % i == 0:
            h += 1
            break

print("Part two: %d" % h)
