input = 344

current = 0
lock = [0]
for x in range(2017):
 next = (current + input) % (x + 1) + 1
 lock.insert(next, x + 1)
 current = next

current += 1
one = lock[current]

current = 0
two = 0
for x in range(50000000):
    next = (current + input) % (x + 1) + 1
    if next == 1:
        two = x + 1
    current = next

print("Part one: %d" % one)
print("Part two: %d" % two)
