tree = [int(x) for x in open("inputs/day08.input").read().split()]


def node(branch):
    children, metadata = branch[:2]
    branch = branch[2:]
    sum_meta = 0
    for x in range(children):
        meta, branch = node(branch)
        sum_meta += meta
    sum_meta += sum(branch[:metadata])
    return sum_meta, branch[metadata:]


total, left = node(tree)
print("1: %d" % total)
