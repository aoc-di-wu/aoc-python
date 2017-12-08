input = []
highestValue = 0
with open('inputs/day08.input','r') as f:
    values= {}
    for line in f:
        name1, modify, value1, _, name2, sign, value2 = line.split(" ")
        value1 = int(value1)
        value2 = int(value2)

        if(name2 not in values):
            values[name2] = 0
        if(name1 not in values):
            values[name1] = 0

        if(eval(str(values[name2]) + sign + str(value2)) == True):
            if(modify == "inc"):
                values[name1] += value1
            else:
                values[name1] -= value1
        if(values[name1] > highestValue):
            highestValue = values[name1]

max = 0
for n in values:
    if(values[n] > max):
        max = values[n]

print("Part one: %d" % max)
print("Part two: %d" % highestValue)
