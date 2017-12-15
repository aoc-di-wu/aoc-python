startA = 512
startB = 191

def calc1(it):
    count = 0
    a = startA
    b = startB
    for x in range(it):
        a *= 16807
        a %= 2147483647

        binA = bin(a)[len(bin(a)) - 16:]

        b *= 48271
        b %= 2147483647

        binB = bin(b)[len(bin(b)) - 16:]
        if(binA == binB):
            count += 1
    return count

def calc2(it):
    count = 0
    a = startA
    b = startB
    for x in range(it):
        while True:
            a *= 16807
            a %= 2147483647
            if(a % 4 == 0):
                break
        binA = bin(a)[len(bin(a)) - 16:]
        while True:
            b *= 48271
            b %= 2147483647
            if(b % 8 == 0):
                break
        binB = bin(b)[len(bin(b)) - 16:]
        if (binA == binB):
            count += 1
    return count

print("Part one: %d" % calc1(40000000))
print("Part two: %d" % calc2(5000000))
