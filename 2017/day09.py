with open('inputs/day09.input','r') as f:
    total = 0
    waste = False
    wasteCount = 0
    skipNext = False
    countOpen = 0
    for line in f:
        for char in line:
            if(not skipNext):
                if(char == "!"):
                    skipNext = True
                elif(char == "<" and not waste):
                    waste = True
                elif(char == ">"):
                    waste = False
                elif(char == "{" and not waste):
                    countOpen += 1
                    total += countOpen
                elif(char == "}" and not waste):
                    countOpen -= 1
                elif(waste):
                    wasteCount += 1

            else:
                skipNext = False

print("Part one: %d" % total)
print("Part two: %d" % wasteCount)
