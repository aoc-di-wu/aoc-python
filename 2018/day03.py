cloth, count = {}, 0
for line in open("inputs/day03.input").read().splitlines():
    id, _, offset, size = line.split()
    offset = str(offset).strip(":").split(",")
    size = str(size).split("x")

    for x in range(int(offset[0]), int(offset[0]) + int(size[0])):
        for y in range(int(offset[1]), int(offset[1]) + int(size[1])):
            coord = (x, y)
            if coord not in cloth:
                cloth[coord] = 1
            elif cloth[coord] == 1:
                cloth[coord] += 1
                count += 1

print("1: %d" % count)

for line in open("inputs/day03.input").read().splitlines():
    id, _, offset, size = line.split()
    offset = str(offset).strip(":").split(",")
    size = str(size).split("x")

    overlap = False
    for x in range(int(offset[0]), int(offset[0]) + int(size[0])):
        for y in range(int(offset[1]), int(offset[1]) + int(size[1])):
            coord = (x, y)
            if cloth[coord] > 1:
                overlap = True
                break

    if not overlap:
        print("2: %s" % str(id).strip("#"))
        break
