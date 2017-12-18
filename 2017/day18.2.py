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

r1 = {"a": 0, "b": 0, "f": 0, "i": 0, "l": 0, "p": 0}
r2 = {"a": 0, "b": 0, "f": 0, "i": 0, "l": 0, "p": 1}

def getValue(v, r):
    try:
        return int(v)

    except ValueError:
        return r[v]

que1 = []
que2 = []
stop = [False, False]

count = 0
def run(reg, i):
    global count

    if(reg == 0):
        register = r1
        recover = que1
    else:
        register = r2
        recover = que2

    if(i < 0 or i >= len(input)):
        stop[reg] = True
        return

    cmd = input[i]

    if cmd[0] == "snd":
        if reg == 0:
            que2.insert(0, getValue(cmd[1], register))
        else:
            que1.insert(0, getValue(cmd[1], register))
            count += 1

    elif cmd[0] == "set":
        register[cmd[1]] = getValue(cmd[2], register)
    elif cmd[0] == "add":
        register[cmd[1]] += getValue(cmd[2], register)
    elif cmd[0] == "mul":
        register[cmd[1]] *= getValue(cmd[2], register)
    elif cmd[0] == "mod":
        register[cmd[1]] %= getValue(cmd[2], register)

    elif cmd[0] == "rcv":
       if len(recover) == 0:
           stop[reg] = True
           return i
       else:
           stop[reg] = False
           register[cmd[1]] = recover.pop()

    elif cmd[0] == "jgz":
        if getValue(cmd[1], register) > 0:
            return i + getValue(cmd[2], register)

reg1 = 0
reg2 = 0
while not (stop[0] and stop[1]):
    r = run(0,reg1)
    if r is not None:
        reg1 = r
    else:
        reg1 += 1

    r = run(1,reg2)
    if r is not None:
        reg2 = r
    else:
        reg2 += 1

print("Part two: %d" % count)
