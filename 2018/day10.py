stars = [list(map(int, line.lstrip("position=< ").rstrip(">\n").replace("> velocity=<", ", ").split(", "))) for line in open("inputs/day10.input")]

d, x1, x2, y1, y2, idx = 999999, 0, 0, 0, 0, 0
for i in range(99999):
    minX = min([x + i * v for x, _, v, _ in stars])
    maxX = max([x + i * v for x, _, v, _ in stars])
    minY = min([y + i * v for _, y, _, v in stars])
    maxY = max([y + i * v for _, y, _, v in stars])
    dist = maxX - minX + maxY - minY
    if dist < d:
        d = dist
        x1, x2 = minX, maxX
        y1, y2 = minY, maxY
    else:
        idx = i - 1
        break

grid = [["." for x in range(x2 - x1 + 1)] for y in range(y2 - y1 + 1)]
final = [[x + idx * vx - x1, y + idx * vy - y1] for x, y, vx, vy in stars]
for star in final:
    x, y = star
    grid[y][x] = "#"

print("1:")
for row in grid:
    print("".join(row))

print("2: %d" % idx)
