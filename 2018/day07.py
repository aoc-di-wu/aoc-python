abc = sorted([chr(ord("A") + x) for x in range(26)])
steps, amount = dict((x, set()) for x in abc), dict((x, 0) for x in abc)
for line in open("inputs/day07.input"):
    l = line.split()
    before, after = l[1], l[7]
    steps[after].add(before)
    amount[after] += 1

done, order = set(), ""
while abc:
    for idx, value in enumerate(abc):
        if not (steps[value] - done):
            order += value
            done.add(value)
            del abc[idx]
            break
print("1: %s" % order)

abc = sorted([chr(ord("A") + x) for x in range(26)])
steps, amount = dict((x, set()) for x in abc), dict((x, 0) for x in abc)
for line in open("inputs/day07.input"):
    l = line.split()
    before, after = l[1], l[7]
    steps[before].add(after)
    amount[after] += 1

time, queue, work = 0, [], []
for x in abc:
    if amount[x] == 0:
        queue.append(x)
while len(work) < 5 and queue:
    x = min(queue)
    queue.remove(x)
    t = time + 61 + ord(x) - ord("A")
    work.append((t, x))

while work or queue:
    time, x = min(work)
    work.remove((time, x))
    for y in steps[x]:
        amount[y] -= 1
        if amount[y] == 0:
            queue.append(y)
    while len(work) < 5 and queue:
        x = min(queue)
        queue.remove(x)
        t = time + 61 + ord(x) - ord("A")
        work.append((t, x))
print("2: %d" % time)
