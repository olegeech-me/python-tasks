def move_zeros(array):
    return [x for x in array if x != 0] + [0 for x in range(array.count(0))]
