input = ""
with open('inputs/day10.input','r') as f:
    for line in f:
        for word in line.split():
            input += word

lengths = []

for c in range(len(input)):
    lengths.append(ord(input[c]))

for x in [17, 31, 73, 47, 23]:
    lengths.append(x)

input = lengths

list = []
for x in range(256):
    list.append(x)

index = 0
skipsize = 0

rounds = 0
while(rounds < 64):
    inputIndex = 0

    for i in input:
        length = input[inputIndex]
        sublist = []
        for y in range(length):
            step = index + y
            while (step >= len(list)):
                step -= len(list)
            sublist.append(list[step])
        sublist.reverse()

        for z in range(length):
            lstep = index + z
            while (lstep >= len(list)):
                lstep -= len(list)
            list[lstep] = sublist[z]

        index += length + skipsize
        while (index >= len(list)):
            index -= len(list)
        inputIndex += 1
        skipsize += 1
    rounds += 1

xorlist = []
for x in range(16):
    xor = 0
    for y in range(16):
        xor = xor ^ list[y + x*16]
    xorlist.append(xor)

hexlist = []
for x in xorlist:
    hexlist.append(hex(x)[2:].rjust(2, "0"))

hex = ""
for x in hexlist:
    hex += x

print("Part two: %s" % hex)
