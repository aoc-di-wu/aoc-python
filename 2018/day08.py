tree = [int(x) for x in open("inputs/day08.input").read().split()]


def node(branch):
    children, metadata = branch[:2]
    branch = branch[2:]
    sum_meta, values = 0, []
    for x in range(children):
        meta, branch, v = node(branch)
        sum_meta += meta
        values.append(v)
    sum_meta += sum(branch[:metadata])

    if children == 0:
        return sum_meta, branch[metadata:], sum(branch[:metadata])
    else:
        v = 0
        for x in branch[:metadata]:
            if 0 < x <= len(values):
                v += values[x - 1]
        return sum_meta, branch[metadata:], v


total, left, value = node(tree)
print("1: %d" % total)
print("2: %d" % value)
