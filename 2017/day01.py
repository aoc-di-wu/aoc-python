i = open('inputs/day01.input', 'r')
input = i.read()

sum = 0
for x in range(len(input) - 1):
    if(input[x] == input[x + 1]):
        sum += int(input[x])

if(input[0] == input[len(input) - 1]):
    sum += int(input[0])

print("Part one: %d" % sum)

sum = 0
half = int(len(input)/2)
for x in range(half):
    if(input[x] == input[x + half]):
        sum += (int(input[x]) * 2)

print("Part two: %d" % sum)
