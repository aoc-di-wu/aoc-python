input = []
with open('inputs/day24.input','r') as f:
    for line in f:
        a, b = line.split('/')
        input.append((int(a), int(b)))

bridges = []
strongest = 0
longest = ["", 0]

def port(left, previous, list, strength):
    global strongest
    global longest

    for x in left:
        if(x[0] == previous):
            next = x[1]
            l = left.copy()
            l.remove(x)
            s = list
            s += str(x[0]) + "/" + str(x[1]) + " "
            st = strength
            st += x[0] + x[1]

            if(st > strongest):
                strongest = st

            if(len(s) >= len(longest[0])):
                if(st > longest[1]):
                    longest = [s, st]

            port(l, next, s, st)

        elif(x[1] == previous):
            next = x[0]
            l = left.copy()
            l.remove(x)
            s = list
            s += str(x[0]) + "/" + str(x[1]) + " "
            st = strength
            st += x[0] + x[1]

            if(st > strongest):
                strongest = st

            if(len(s) >= len(longest[0])):
                if(st > longest[1]):
                    longest = [s, st]

            port(l, next, s, st)


left = input.copy()
port(left, 0, "", 0)

print("Part one: %d" % strongest)
print("Part two: %d" % longest[1])






