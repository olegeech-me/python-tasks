def find_it(seq):
    res = {}
    for x in seq:
        res[x] = res.get(x, 0) + 1
    for k, v in res.items():
        if v % 2 == 1:
            return k
    return None


print(find_it([1, 2, 2, 2, 3, 3]))
