"""
Write a function that takes a positive integer and returns the next smaller positive
integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 when there is no smaller number that contains the same digits.
Also return -1 when the next smaller number with the same digits would require the
leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.

1 2 6 2 3 4 7
^ ^ ^ ^ ^ ^ ^
0 1 2 3 4 5 6
    ^     ^ ^
    X     Y last
    ^ swap^      =  1 2 4 2 3 6 7      =>   1247632
                        ^ | _ _ |
                        Y  sort descending
"""


def next_smaller(num):
    nums = [int(x) for x in str(num)]
    res = []
    size = len(str(num))
    for i in range(size - 2, -1, -1):
        for j in range(size - 1, i, -1):
            x = int(str(num)[i])
            y = int(str(num)[j])
            print(f"x={x}, y={y}, i={i}, j={j}")
            if x > y:
                print(f"Got x,y = ({x},{y})")
                res = list(nums)
                res[i] = y
                res[j] = x
                print("Result after swap:", res)
                if res[0] == 0:
                    print("Cannot have number starting with 0:", res)
                    return -1

                res = res[: i + 1] + sorted(res[i + 1 :], reverse=True)
                print("Result after sort:", res)
                break
        if res:
            break

    if res:
        return int("".join(str(x) for x in res))
    else:
        return -1


print(next_smaller(1262347))
print(next_smaller(135))
print(next_smaller(1027))
print(next_smaller(328700))
