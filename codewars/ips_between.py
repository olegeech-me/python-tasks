"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between
them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be
greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50
* With input "10.0.0.0", "10.0.1.0"   => return  256
* With input "20.0.0.10", "20.0.1.0"  => return  246
"""


def ips_between(start, end):
    ip1_address_space = [(256 - int(x)) for x in start.split(".")]
    ip2_address_space = [(256 - int(x)) for x in end.split(".")]
    diff = [int(ip1) - int(ip2) for ip1, ip2 in zip(ip1_address_space, ip2_address_space)]
    result = diff[0] * 2 ** 24 + diff[1] * 2 ** 16 + diff[2] * 2 ** 8 + diff[3]

    print(ip1_address_space, ip2_address_space)
    print(diff)
    print(result)
    return result


ips_between("10.0.0.0", "10.0.0.50")
ips_between("10.0.0.0", "10.0.1.0")
ips_between("20.0.0.10", "20.0.1.0")
