input = []
with open('inputs/day06.input','r') as f:
    for line in f:
        for word in line.split():
            w = int(word)
            input.append(w)

max = 0
current = 0
seen = []

while(str(input) not in seen):
    seen.append(str(input))
    for x in range(len(input) -1, -1, -1):
        if(input[x] >= max):
            max = input[x]
            current = x
    input[current] = 0
    poss = current + 1
    while(max > 0):
        if(poss < len(input)):
            input[poss] += 1
            max -= 1
            poss += 1
        elif(poss >= len(input)):
            poss -= len(input)
            input[poss] +=1
            max -= 1
            poss += 1

for x in range(len(seen)):
    if(seen[x] == str(input)):
        current = x
        break

print("Part one: %d" % len(seen))
print("Part two: %d" % (len(seen) - current))
