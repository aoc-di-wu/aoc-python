input = []
with open('inputs/day05.input','r') as f:
    for line in f:
        for word in line.split():
            w = int(word)
            input.append(w)

sum = 0
pos = 0

loop = True
while(loop):
    if(pos < len(input)):
        input[pos] += 1
        pos += input[pos] - 1
        sum += 1
    else:
        loop = False

print("Part one: %d" % sum)
