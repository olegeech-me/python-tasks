ipa = "127.0.0.1"

print(ipa)

parts = ipa.split(".")
print()

print()
print("Dec Hex Binary  Oct")
for part in parts:
    print(
        format(int(part), "03d"),
        format(int(part), "02x"),
        format(int(part), "08b"),
        format(int(part), "03o"),
    )
print()
print()


hexNumber = (
    format(int(parts[0]), "02X")
    + format(int(parts[1]), "02X")
    + format(int(parts[2]), "02X")
    + format(int(parts[3]), "02X")
)

print()
print("IP Address in HEX base 16")
print("0x" + hexNumber)


print()
print()
print("IP Address in HEX2 using a for loop")
hex2 = "0x"

for part in parts:
    hex2 += format(int(part), "02x")

print(hex2)


print()
print()
print("IP Address in Decimal ")
print(int(hex2, base=16))

binaryNumber = (
    format(int(parts[0]), "08b")
    + format(int(parts[1]), "08b")
    + format(int(parts[2]), "08b")
    + format(int(parts[3]), "08b")
)

print()
print()
print("IP Address in binary ")
print("0b" + binaryNumber)
print()
print()

bin2 = "0b"

for part in parts:
    bin2 += format(int(part), "08b")

print("IP Address in binary using for loop")
print(bin2)
print()
print()
