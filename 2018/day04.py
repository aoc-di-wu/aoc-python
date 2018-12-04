lines = sorted(open("inputs/day04.input").read().splitlines())
guards = {}
for line in lines:
    if line[25] == "#":
        guard = line.split()[3]
    elif line[25] == "a":
        asleep = int(line[15:17])
    else:
        wakeup = int(line[15:17])
        if guard not in guards:
            guards[guard] = [0 for x in range(60)]
        for sec in range(asleep, wakeup):
            guards[guard][sec] += 1

most, freq = {}, {}
for guard in guards:
    most[sum(guards[guard])] = guard
    freq[max(guards[guard])] = guard

guard1 = most[sorted(most, reverse=True)[0]]
guard2 = freq[sorted(freq, reverse=True)[0]]
print("1: %d" % (int(guard1.strip("#")) * guards[guard1].index(max(guards[guard1]))))
print("2: %d" % (int(guard2.strip("#")) * guards[guard2].index(max(guards[guard2]))))
