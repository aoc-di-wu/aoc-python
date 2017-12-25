input = []
with open('inputs/day25.input','r') as f:
    for line in f:
        input.append(line.strip(" ").strip("\n").lower())

blueprint = {}
state = ""
value = 0
for x in input:
    if(x[:5] == "begin"):
        state = x[len(x) - 2: len(x) - 1]
        blueprint["state"] = state
    elif(x[:7] == "perform"):
        steps = str(x).strip("perform a diagnostic checksum after ").strip(" steps.")
        blueprint["steps"] = int(steps)
    if(x[:2] == "in"):
        state = x[len(x) - 2: len(x) - 1]
        blueprint[state] = {}
    elif(x[:2] == "if"):
        value = int(x[len(x) - 2: len(x) - 1])
    elif(x[:3] == "- w"):
        blueprint[state][value] = [int(x[len(x) - 2: len(x) - 1])]
    elif(x[:3] == "- m"):
        if(x[len(x) - 3: len(x) - 1] == "ft"):
            blueprint[state][value].append(-1)
        else:
            blueprint[state][value].append(1)
    elif(x[:3] == "- c"):
        blueprint[state][value].append(x[len(x) - 2: len(x) - 1])

state = blueprint["state"]
steps = blueprint["steps"]

tape = {}
current = 0

for x in range(steps):
    if (current not in tape):
        tape[current] = 0

    bp = blueprint[state][tape[current]]

    tape[current] = bp[0]
    current += bp[1]
    state = bp[2]

checksum = 0
for x in tape:
    checksum += tape[x]

print("Part one: %d" % checksum)
