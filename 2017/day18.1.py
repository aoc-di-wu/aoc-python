input = []
with open('inputs/day18.input','r') as f:
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

r = {'a': 0, 'b': 0, 'f': 0, "i": 0, "l": 0, "p": 0}

send = 0
recover = 0

def getValue(v):
    try:
        return int(v)

    except ValueError:
        return r[v]

cur = 0
while True:
    if(input[cur][0] == "snd"):
        value = getValue(input[cur][1])
        sound = value

    elif(input[cur][0] == "set"):
        register = input[cur][1]
        value = getValue(input[cur][2])

        r[register] = value

    elif(input[cur][0] == "add"):
        register = input[cur][1]
        value = getValue(input[cur][2])

        r[register] += value

    elif (input[cur][0] == "mul"):
        register = input[cur][1]
        value = getValue(input[cur][2])

        r[register] *= value

    elif (input[cur][0] == "mod"):
        register = input[cur][1]
        value = getValue(input[cur][2])

        r[register] %= value

    elif (input[cur][0] == "rcv"):
        value = getValue(input[cur][1])
        if(value != 0):
            recover = sound
            break

    elif (input[cur][0] == "jgz"):
        register = input[cur][1]
        value = getValue(input[cur][2])

        if(r[register] > 0):
            cur += (value - 1)
        elif(r[register] < 0):
            cur += value

    cur += 1
    if(cur >= len(input)):
        break

print("Part one: %d" % recover)

