serial = 7139


def power_level(x, y, sn=serial):
    idx = x + 10
    lvl = idx * y + sn
    lvl *= idx
    dgt = lvl // 100 % 10
    return dgt - 5


largest = 0
coordinates = 0, 0
for i in range(301):
    for j in range(301):
        level = sum([power_level(i + x, j + y) for x in range(3) for y in range(3)])
        if level > largest:
            largest = level
            coordinates = i, j
print("1: %d,%d" % coordinates)

largest = 0
coordinates = 0, 0, 0
print("\n   ~-_ go make")
print("  _-~   some")
print("c|_|   coffee... \n")
for size in range(1, 21):
    for i in range(301 - size):
        for j in range(301 - size):
            level = sum([power_level(i + x, j + y) for x in range(size) for y in range(size)])
            if level > largest:
                largest = level
                coordinates = i, j, size
print("2: %d,%d,%d" % coordinates)
