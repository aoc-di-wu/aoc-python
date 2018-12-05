line = open("inputs/day05.input").read().strip()

lowerABC = [chr(ord("a") + x) for x in range(0, 26)]

new = None
while new != line:
    new = line
    for x in lowerABC:
        line = line.replace(x + x.upper(), "")
        line = line.replace(x.upper() + x, "")
print("1: %d" % len(line))

initial, best = line, len(line)
for x in lowerABC:
    line = initial
    line = line.replace(x, "")
    line = line.replace(x.upper(), "")
    new = None  # same as part one
    while new != line:
        new = line
        for x in lowerABC:
            line = line.replace(x + x.upper(), "")
            line = line.replace(x.upper() + x, "")
    if len(line) < best:
        best = len(line)
print("2: %d" % best)
