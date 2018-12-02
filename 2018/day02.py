count = [0, 0]
for line in open("inputs/day02.input").read().splitlines():
    contains, two, three = {}, False, False
    for letter in line:
        if letter not in contains:
            contains[letter] = 1
        else:
            contains[letter] += 1
    for l in contains:
        if contains[l] == 2:
            two = True
        if contains[l] == 3:
            three = True
    if two:
        count[0] += 1
    if three:
        count[1] += 1
print("1: %d" % (count[0] * count[1]))

l, found = open("inputs/day02.input").read().splitlines(), False
for i, line1 in enumerate(l):
    for j, line2 in enumerate(l):
        count, differ = 0, ""
        if i != j:
            for x in range(len(line1)):
                if line1[x] != line2[x]:
                    count += 1
                    differ = line1[:x] + line1[x + 1:]
                if count > 1:
                    break
        if count < 2 and count != 0:
            print("2: %s" % differ)
            found = True
            break
    if found:
        break
