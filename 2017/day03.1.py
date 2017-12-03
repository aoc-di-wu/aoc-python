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

steps = 0

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

        if(tcount == input):
            grid[middleY][middleX] = 0
            if(middleX - middle >= 0):
                steps += (middleX - middle)
            elif(middleX - middle < 0):
                steps -= (middleX - middle)

            if(middleY - middle >= 0):
                steps += (middleY - middle)
            elif(middleY - middle < 0):
                steps -= (middleY - middle)
        else:
            grid[middleY][middleX] = tcount
        count += 1
        tcount += 1

print("Part one: %d" % steps)
