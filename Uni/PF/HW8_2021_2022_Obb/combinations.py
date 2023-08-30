def permutations(seq, mem):
    if not seq:
        return []

    if len(seq) == 1:
        return [seq]

    perm = []

    for i in range(len(seq)):
        start = seq[i:i + 1]
        red = seq[:i] + seq[i + 1:]

        if tuple(start + red) in mem:
            continue

        mem.add(tuple(start + red))

        perm += [start + p for p in permutations(red, set())]

    return perm


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat

    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        
#print(list(product([0, 128, 196, 255], repeat=3)))

# p_set = set()

for p in permutations([0, 255], set()):
    print(p)
    p_set.add(tuple(p))

# for p in permutations([255, 0, 0, 0], set()):
#     print(p)
#     p_set.add(tuple(p))

# for p in permutations([255, 255, 0, 0], set()):
#     print(p)
#     p_set.add(tuple(p))

# for p in permutations([255, 255, 255, 0], set()):
#     print(p)
#     p_set.add(tuple(p))

# for p in permutations([255, 255, 255, 255], set()):
#     print(p)
#     p_set.add(tuple(p))

# #print(p_set, len(p_set))