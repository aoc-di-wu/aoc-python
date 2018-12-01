print("1: %d" % sum(int(x) for x in open("inputs/day01.input").read().splitlines()))

freq, f = {}, 0
while f not in freq:
    for x in open("inputs/day01.input").read().splitlines():
        if f not in freq:
            freq[f] = 1
        else:
            print("2: %d" % f)
            break
        f += int(x)
