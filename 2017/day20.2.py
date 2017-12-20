input = []
with open('inputs/day20.input', 'r') as f:
    for line in f:
        l = ""
        for char in line:
            if not char in " pva=<>\n":
                l += char
        l = l.split(',')
        line = []
        count = 0
        vector = []
        for x in range(len(l)):
            count += 1
            vector.append(int(l[x]))
            if(count == 3):
                line.append(vector)
                vector = []
                count = 0
        input.append(line)

for c in range(50):
    for x in range(len(input)):
        for y in range(3):
            input[x][1][y] += input[x][2][y]
            input[x][0][y] += input[x][1][y]

    remove = []
    for x in range(len(input)):
        for z in range(len(input)):
            if(z != x and input[x][0] == input[z][0]):
                if(x not in remove):
                    remove.append(x)
    remove.reverse()
    for x in remove:
        input.pop(x)

print("Part two: %d" % len(input))
