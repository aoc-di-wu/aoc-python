input = open('inputs/day16.input').read().strip().split(',')

positions = list("abcdefghijklmnop")

def move(iterations, pos):
    sequence = []
    for i in range(iterations):
        s = ''.join(pos)
        if s in sequence:
            return sequence[iterations % i]
        sequence.append(s)

        for i in input:
            if i[0] == 's':
                x = int(i[1:])
                pos = pos[-x:] + pos[:-x]
            elif i[0] == 'x':
                x = i[1:].split('/')
                a, b = int(x[0]), int(x[1])
                pos[a], pos[b] = pos[b], pos[a]
            elif i[0] == 'p':
                a, b = i[1:].split('/')
                A = pos.index(a)
                B = pos.index(b)
                pos[A], pos[B] = pos[B], pos[A]

    return ''.join(pos)

print("Part one: %s" % move(1, positions[:]))
print("Part two: %s" % move(1000000000, positions[:]))
