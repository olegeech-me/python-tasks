"""
This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
plus, minus, times, divided_by.

Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents
the right operand. Division should be integer division.

For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def renderer(right_side, num):
    if right_side:
        exec("x = " + num + right_side)
        return locals()["x"]
    else:
        return num


def zero(arg=None):
    return renderer(arg, "0")


def one(arg=None):
    return renderer(arg, "1")


def two(arg=None):
    return renderer(arg, "2")


def three(arg=None):
    return renderer(arg, "3")


def four(arg=None):
    return renderer(arg, "4")


def five(arg=None):
    return renderer(arg, "5")


def six(arg=None):
    return renderer(arg, "6")


def seven(arg=None):
    return renderer(arg, "7")


def eight(arg=None):
    return renderer(arg, "8")


def nine(arg=None):
    return renderer(arg, "9")


def plus(x):
    return " + " + x


def minus(x):
    return " - " + x


def times(x):
    return " * " + x


def divided_by(x):
    return " // " + x


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
print(eight(divided_by(three())))
