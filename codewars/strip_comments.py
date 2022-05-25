"""
Complete the solution so that it strips all text that follows any of a set of
comment markers passed in. Any whitespace at the end of the line should also
be stripped out.
Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples, pears\ngrapes\nbananas"
"""

import re


def strip_comments(text, markers):
    if not markers:
        return text
    result = []
    markers_range = "|".join([re.escape(m) for m in markers])
    regexp = f"\\s*(:?{markers_range}).*$"
    for line in text.split("\n"):
        result.append(re.sub(regexp, "", line))
    return "\n".join(result)


# print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
# print(
#    strip_comments(
#        "avocados cherries ^ ? lemons\npears lemons\nwatermelons pears lemons ^\n!",
#        ["^", ".", "@", "!", "-", "=", "?"],
#    )
# )

print(
    strip_comments(
        "  watermelons ! pears watermelons\n# @ strawberries lemons watermelons pears\nlemons # - lemons\nlemons = apples ? avocados =\napples bananas oranges strawberries # @",
        ["!", "^", ",", "-", "'", "?", ".", "="],
    )
)
