input = "wenycdww"

def knot_hash(lengths):
    list = []
    for x in range(256):
        list.append(x)

    inputIndex = 0

    index = 0
    skipsize = 0

    rounds = 0
    while (rounds < 64):
        inputIndex = 0

        for i in lengths:
            length = lengths[inputIndex]
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
            xor = xor ^ list[y + x * 16]
        xorlist.append(xor)

    hexlist = []
    for x in xorlist:
        hexlist.append(hex(x)[2:].rjust(2, "0"))

    tothex = ""
    for x in hexlist:
        tothex += x

    return tothex

list = []
for x in range(128):
    row = []
    for y in input:
        row.append((ord(y)))
    row.append((ord("-")))
    for z in str(x):
        row.append(ord(z))
    row += [17, 31, 73, 47, 23]
    list.append(row)


blist = []
for x in range(len(list)):
    h = knot_hash(list[x])
    row = []
    for y in h:
        b = bin(int(y, 16))[2:].zfill(4)
        for l in range(len(b)):
            row.append(int(b[l]))
    blist.append(row)

sum = 0
for x in blist:
    for y in x:
        sum += int(y)

def regions(i, j):
    if(i < 0 or j < 0 or i >= len(blist) or j >= len(blist[i]) or blist[i][j] == 0):
        return 0
    else:
        blist[i][j] = 0
        regions(i + 1, j)
        regions(i - 1, j)
        regions(i, j + 1)
        regions(i, j - 1)
        return 1

sumr = 0
for i in range(len(blist)):
    for j in range(len(blist[i])):
        sumr += regions(i, j)

print("Part one: %d" % sum)
print("Part two: %d" % sumr)


