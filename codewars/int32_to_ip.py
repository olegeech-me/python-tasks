"""
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it
as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and
returns a string representation of its IPv4 address.

Examples
2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"


1		0		1		1
1x2^3	+	0x2^2	+	1x2^1	+	1x2^0	=
8	+	0	+	2	+	1	=	11

"""


def int32_to_ip(int32):
    binary = format(int32, "032b")
    res = ".".join([str(int(binary[i : i + 8], 2)) for i in range(0, 32, 8)])
    print(res)
    return res


def ip_int32(ip):
    octs = list(map(int, ip.split(".")))
    # int32 = (o[0] * pow(256, 3)) + (o[1] * pow(256, 2)) + (o[2] * 256) + o[3]
    binary = "0b"
    for oct in octs:
        binary += format(int(oct), "08b")
    int32 = int(binary, 2)
    print(int32)
    return int32


int32_to_ip(2149583361)
int32_to_ip(32)
