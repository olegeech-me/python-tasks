def add_binary(a, b):
    return bin(a + b).replace("0b", "")


print(add_binary(5, 9))
