input = 347991

from math import sqrt

loop = True
spirals = 1
grid = []

while(loop):
    if(input <= spirals**2):
        loop = False
    else:
        spirals += 2

for x in range(spirals):
    subgrid = []
    for y in range(spirals):
        subgrid.append(0)
    grid.append(subgrid)

middle = int((spirals - 1)/2)
tcount = 1
middleX = middle - 1
middleY = middle

largev = 0
novalue = True

for x in range(middle + 1):
    count = 0
    size = (2*x + 1)**2
    row = sqrt(size)
    rcorner = row - 1

    for y in range(size):

        if(tcount == 1):
            middleX += 1
        else:
            if(count == 0):
                middleX += 1
            elif(count > 0 and count < rcorner):
                middleY -= 1
            elif(count >= rcorner and count < 2*rcorner):
                middleX -= 1
            elif(count >= 2*rcorner and count < 3*rcorner):
                middleY += 1
            elif(count >= 3*rcorner and count < 4*rcorner):
                middleX += 1
            elif(count == 4*rcorner):
                break

        if(tcount == 1):
            grid[middleY][middleX] = 1
        else:
            adj = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if(middleX + x < spirals and middleX + x >= 0 and
                            middleY + y < spirals and middleY + y >= 0):
                        adj += grid[middleY + y][middleX + x]
                        if(novalue and adj > input):
                            largev = adj
                            novalue = False
            grid[middleY][middleX] = adj

        count += 1
        tcount += 1

        if(not novalue):
            break
    if (not novalue):
        break

print("Part two: %d" % largev)
