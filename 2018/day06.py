coordinates = [list(map(int, line.split(", "))) for line in open("inputs/day06.input")]
abc = [chr(ord(y) + x) for y in ["a", "A"] for x in range(26)]
coords = {}
for idx, c in enumerate(coordinates):
    coords[(c[0], c[1])] = abc[idx]

top, right, bottom, left = 99999, 0, 0, 99999
for coord in coords:
    x, y = coord
    top = min(top, y)
    right = max(right, x)
    bottom = max(bottom, y)
    left = min(left, x)

# grid[y][x]
grid = [["." for x in range(0, right + left)] for y in range(0, bottom + top)]
for i in range(right + left):
    for j in range(bottom + top):
        shortest, coord = 9999, None
        for c in coords:
            x, y = c
            d = abs(x - i) + abs(y - j)
            if d < shortest:
                shortest = d
                coord = c
            elif d == shortest:
                coord = None
        if coord is not None:
            grid[j][i] = coords[coord]

finite = dict(coords)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if x == left or x == right or y == top or y == bottom:
            char = grid[y][x]
            for coord in coords:
                if coords[coord] == char:
                    if coord in finite:
                        del finite[coord]
                    else:
                        break


finite = dict((v, 0) for k, v in finite.items())
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] in finite:
            finite[grid[y][x]] += 1

largest = 0
for _, count in finite.items():
    largest = max(largest, count)
print("1: %d" % largest)

# print grid
# for y in range(len(grid)):
#     s = ""
#     for x in grid[y]:
#         s += x
#     print(s)

region = 0
for i in range(right + left):
    for j in range(bottom + top):
        count = 0
        for coord in coords:
            x, y = coord
            count += (abs(x - i) + abs(y - j))
        if count < 10000:
            region += 1
print("2: %d" % region)
