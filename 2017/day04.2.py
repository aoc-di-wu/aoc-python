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
    words = []
    for word1 in array:
        letters = []
        for l in range(len(word1)):
            letters.append(word1[l])
        letters.sort()
        words.append(letters)

    for w in words:
        i = words.index(w)
        words.remove(w)
        for word2 in words:
            if(word2 == w):
                count += 1
        words.insert(i, w)

    if(count == 0):
        sum += 1

print("Part two: %d" % sum)
