def square_digits(num):
    res = ""
    for x in str(num):
        res += str(int(x) ** 2)
    return int(res)


print(square_digits(9119))
