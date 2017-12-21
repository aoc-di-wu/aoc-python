input = open('inputs/day21.input', 'r').read()
lines = input.splitlines()

rules = {}

def rotate(line):
    if(len(line) == 5):
        return line[1] + line[4] + "/" + line[0] + line[3]
    else:
        rotated = line[2] + line[6] + line[10] + "/" + line[1] + line[5] + line[9]
        return rotated + "/" + line[0] + line[4] + line[8]

def mirror(line):
    rotated = line[2] + line[1] + line[0] + "/" + line[6] + line[5] + line[4]
    return rotated + "/" + line[10] + line[9] + line[8]

for l in lines:
    part = l.split(" => ")

    rules[part[0]] = part[1]

    rotated = rotate(part[0])
    rules[rotated] = part[1]
    for x in range(2):
        rotated = rotate(rotated)
        rules[rotated] = part[1]

    if(len(part[0]) == 11):
        rotated = mirror(rotated)
        rules[rotated] = part[1]

        for x in range(3):
            rotated = rotate(rotated)
            rules[rotated] = part[1]

def iterate(i):
    grid = ".#.\n..#\n###".splitlines()

    for x in range(i):
        if(len(grid) % 2 == 0):
            grid_ = []
            for y in range(int(len(grid)/2)):
                l1 = ""
                l2 = ""
                l3 = ""
                for z in range(int(len(grid)/2)):
                    sub = grid[y*2][z*2:(z+1)*2] + "/" + grid[y*2+1][z*2:(z+1)*2]
                    check = rules[sub].split("/")
                    l1 += check[0]
                    l2 += check[1]
                    l3 += check[2]
                grid_.append(l1)
                grid_.append(l2)
                grid_.append(l3)
            grid = grid_
        else:
            grid_ = []
            for y in range(int(len(grid)/3)):
                l1 = ""
                l2 = ""
                l3 = ""
                l4 = ""
                for z in range(int(len(grid) / 3)):
                    sub = grid[y*3][z*3:(z+1)*3] + "/" + grid[y*3+1][z*3:(z+1)*3] + "/" + grid[y*3+2][z*3:(z+1)*3]
                    check = rules[sub].split("/")
                    l1 += check[0]
                    l2 += check[1]
                    l3 += check[2]
                    l4 += check[3]
                grid_.append(l1)
                grid_.append(l2)
                grid_.append(l3)
                grid_.append(l4)
            grid = grid_

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if(grid[x][y] == "#"):
                count += 1

    return count

print("Part one: %d" % iterate(5))
print("Part two: %d" % iterate(18))
