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

for c in range(1000):
    for x in range(len(input)):
        for y in range(3):
            input[x][1][y] += input[x][2][y]
            input[x][0][y] += input[x][1][y]

zero = 0
sum = 1000000000
for x in range(len(input)):
    pos = 0
    for y in range(3):
        pos += abs(input[x][0][y])
    if(pos < sum):
        sum = pos
        zero = x
print("Part one: %d" % zero)
