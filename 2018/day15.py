def move_character(data, from_row, from_col, to_row, to_col, char):
    data[from_row][from_col], data[to_row][to_col] = ".", (char[0], char[1], True)
    return data


def attack(data, row, col, enemy, damage=3):
    if not adjacent(data, row, col, enemy):
        return data, False

    enemies = {}
    for c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if data[c[0]][c[1]][0] == enemy:
            enemies[c] = data[c[0]][c[1]][1]

    enemies = [x for x in enemies if enemies[x] == min(enemies.values())]
    enemies.sort()

    coord = enemies[0]
    enemy = data[coord[0]][coord[1]]

    points = enemy[1] - damage
    enemy = (enemy[0], points, enemy[2])

    if points <= 0:
        data[coord[0]][coord[1]] = "."
        return data, True
    data[coord[0]][coord[1]] = enemy
    return data, False


def adjacent(data, j, i, enemy):
    if any(x[0] == enemy for x in [data[j + 1][i], data[j - 1][i], data[j][i + 1], data[j][i - 1]]):
        return True
    return False


def best_move(best_moves):
    if not best_moves:
        return None

    best_moves = [x for x in best_moves if x[1] == min([x[1] for x in best_moves])]

    best_moves.sort(key=lambda x: x[2])
    best_moves = [x for x in best_moves if x[2] == best_moves[0][2]]

    best_moves.sort(key=lambda x: x[0])
    best_moves = [x for x in best_moves if x[0] == best_moves[0][0]]

    return best_moves[0][0]


def count_characters(data):
    seen = {"G": 0, "E": 0}
    for row in data:
        for col in row:
            if col[0] in ["G", "E"]:
                seen[col[0]] += 1
    return seen


def bfs_move(inp, j, i, enemy):
    if adjacent(inp, j, i, enemy):
        return None

    first_moves = [x for x in [(j + 1, i), (j - 1, i), (j, i - 1), (j, i + 1)] if inp[x[0]][x[1]] == "."]
    best_moves = []
    for move in first_moves:
        r, c = move
        if adjacent(inp, r, c, enemy):
            best_moves.append((move, 1, move))
            continue

        seen = {(j, i), (r, c)}
        stack = [x for x in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)] if
                 inp[x[0]][x[1]] == "." and (x[0], x[1]) not in seen]

        idx, run = 1, True
        while run:
            idx += 1
            new_stack = []
            for tile in stack:
                if tile in seen:
                    continue

                seen.add(tile)
                r, c = tile

                if adjacent(inp, r, c, enemy):
                    best_moves.append((move, idx, (r, c)))
                    run = False
                    continue
                new_stack += [x for x in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)] if
                              inp[x[0]][x[1]] == "." and (x[0], x[1]) not in seen]

            stack = list(set(new_stack))
            if not stack:
                run = False
    return best_move(best_moves)


def score(data, rounds):
    points = 0
    for row in data:
        for col in row:
            if col[0] in ["G", "E"]:
                points += col[1]
    return rounds * points


def reset(data):
    for j, row in enumerate(data):
        for i, col in enumerate(row):
            if col[0] in ["G", "E"]:
                data[j][i] = (col[0], col[1], False)
    return data


def loop(dmg):
    grid = []
    for j, row in enumerate(open("inputs/day15.input", "r").read().strip().split("\n")):
        grid.append([x for x in row])
        for i, col in enumerate(row):
            if col in ["G", "E"]:
                grid[j][i] = (col, 200, False)

    rounds = 0
    while True:
        counts = count_characters(grid)
        for j, row in enumerate(grid):
            for i, col in enumerate(row):
                char = grid[j][i]
                if isinstance(char, tuple):
                    if char[2]:
                        continue

                    r, c = j, i
                    hero = char[0]
                    enemy = "G" if hero == "E" else "E"

                    counts[hero] -= 1

                    move_to = bfs_move(grid, j, i, enemy)
                    if move_to:
                        r, c = move_to
                        grid = move_character(grid, j, i, r, c, char)

                    grid, death = attack(grid, r, c, enemy, dmg[hero])
                    if death:
                        if enemy == "E" and dmg["E"] != 3:
                            return False
                        game_over = any(x == 0 for x in count_characters(grid).values())
                        if game_over:
                            if counts[hero] > 0:
                                return score(grid, rounds)
                            return score(grid, rounds + 1)
        grid = reset(grid)
        rounds += 1


def battle():
    dmg, score = {"G": 3, "E": 3}, False
    while not score:
        dmg["E"] += 1
        score = loop(dmg)
    return score


print("1: %d" % loop({"G": 3, "E": 3}))
print("2: %d" % battle())
