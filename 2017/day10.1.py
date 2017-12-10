input = []
with open('inputs/day10.input','r') as f:
    for line in f:
        for word in line.split(','):
            w = int(word)
            input.append(w)

list = []
for x in range(256):
    list.append(x)

inputIndex = 0

index = 0
skipsize = 0

for i in input:
    length = input[inputIndex]
    sublist = []
    for y in range(length):
        step = index + y
        while(step >= len(list)):
            step -= len(list)
        sublist.append(list[step])
    sublist.reverse()

    for z in range(length):
        lstep = index + z
        while(lstep >= len(list)):
            lstep -= len(list)
        list[lstep] = sublist[z]

    index += length + skipsize
    while(index >= len(list)):
        index -= len(list)
    inputIndex += 1
    skipsize += 1

mul = list[0]*list[1]

print("Part one: %d" % mul)
