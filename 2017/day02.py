input = []
with open('inputs/day02.input','r') as f:
    for line in f:
        inputline = []
        for word in line.split():
            inputline.append(word)

        input.append(inputline)

number = ""
sum = 0
for x in range(len(input)):
    max = 0
    min = 10000
    row = str(input[x])
    for y in range(len(row)):
        try:
            char = int(row[y])
            number += str(char)

        except ValueError:
            try:
                mm = int(number)
                if (mm > max):
                    max = mm
                if (mm < min):
                    min = mm
                number = ""
            except ValueError:
                number = ""

    sum += (max - min)
print("Part one: %d" % sum)

betterArray = []
for x in range(len(input)):
    bA = []
    row = str(input[x])
    for y in range(len(row)):
        try:
            char =  int(row[y])
            number += str(char)
        except ValueError:
            try:
                value = int(number)
                bA.append(value)
                number = ""
            except ValueError:
                number = ""
    betterArray.append(bA)

sum = 0
for array in betterArray:
    for x in array:
        for y in array:
            if(x is not y):
                if x%y == 0:
                    sum += int(x/y)
print("Part two: %d" % sum)
