import operator


def function_factory(x, y, o):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
    }
    return lambda: ops[o](x, y)


add = function_factory(3, 5, "+")
print(add())
