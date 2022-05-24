def positive_sum(arr):
    return sum(x if x > 0 else 0 for x in arr)


print(positive_sum([1, 2, 3, 4, 5]) == 15)
print(positive_sum([1, -2, 3, 4, 5]) == 13)
print(positive_sum([-1, 2, 3, 4, -5]) == 9)
