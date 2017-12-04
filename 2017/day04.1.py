input = []
with open('inputs/day04.input','r') as f:
    for line in f:
        inputline = []
        for word in line.split():
            inputline.append(word)

        input.append(inputline)

sum = 0
for array in input:
    count = 0
    for word1 in array:
        i = array.index(word1)
        array.remove(word1)
        for word2 in array:
            if(word1 == word2):
                count += 1
        array.insert(i, word1)
    if(count == 0):
        sum += 1

print("Part one: %d" % sum)
