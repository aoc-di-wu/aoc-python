input = []
with open('inputs/day19.input', 'r') as f:
    for line in f:
        line = str(line)
        row = []
        for l in range(len(line) - 1):
            row.append(line[l])
        while(len(row) < 201):
            row.append(" ")

        input.append(row)

x = input[0].index("|")
y = 0

letters = ""
current = "|"
direction = "down"

steps = 0

while current != " ":
    steps += 1
    if(direction == "down"):
        y += 1
    elif(direction == "up"):
        y -= 1
    elif(direction == "right"):
        x += 1
    elif(direction == "left"):
        x -= 1

    current = input[y][x]
    if(current == "+"):
        if(direction == "down" or direction == "up"):
            if(input[y][x + 1] != " "):
                direction = "right"
            else:
                direction = "left"
        else:
            if(input[y + 1][x] != " "):
                direction = "down"
            else:
                direction = "up"
    elif(current != "|" and current != "-"):
        letters += current

print("Part one: %s" % letters)
print("Part two: %d" % steps)
