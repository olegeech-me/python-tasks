"""
Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each
other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable):
    result = []
    for i in range(len(iterable)):
        if i == 0:
            result.append(iterable[i])
        else:
            if iterable[i] != iterable[i - 1]:
                result.append(iterable[i])
            else:
                continue
    return result


# BETTER SOLUTION TO USE groupby() from itertools!
from itertools import groupby

"""
>>> list(groupby("AAAABBBCCDAABBB"))
[('A', <itertools._grouper object at 0x7f1e2f2cfeb0>),
('B', <itertools._grouper object at 0x7f1e2f2cf970>),
('C', <itertools._grouper object at 0x7f1e2f1c3070>),
('D', <itertools._grouper object at 0x7f1e2f1c3250>),
('A', <itertools._grouper object at 0x7f1e2f1c3280>),
('B', <itertools._grouper object at 0x7f1e2f1c32b0>)]
"""

[k for k, g in groupby("AAAABBBCCDAABBB")]


print(
    unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"],
    unique_in_order("ABBCcAD") == ["A", "B", "C", "c", "A", "D"],
    unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3],
)
