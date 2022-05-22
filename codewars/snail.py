"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements
to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""


def snail(matrix: list):
    snail_array = []
    while len(matrix):
        # taking top
        snail_array = snail_array + matrix.pop(0) if snail_array else matrix.pop(0)
        # taking right side
        for i in range(0, len(matrix)):
            snail_array += [matrix[i].pop()]
        # taking bottom side
        if matrix:
            snail_array += reversed(matrix.pop())
        # taking left side
        for i in range(len(matrix) - 1, -1, -1):
            snail_array += [matrix[i].pop(0)]

    return snail_array


array = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]

print(snail(array))
