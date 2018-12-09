import collections


def play(players, last_point):
    circle = collections.deque([0])
    scores, player = dict((x, 0) for x in range(1, players + 1)), 1
    for x in range(1, last_point + 1):
        if (x % 23) == 0:
            circle.rotate(-7)
            scores[player] += x + circle.pop()
        else:
            circle.rotate(2)
            circle.append(x)

        player += 1
        if player > players:
            player = 1
    return max(scores.values())


print("1: %d" % play(448, 71628))
print("2: %d" % play(448, 71628 * 100))
