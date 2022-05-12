def tribonacci(signature, n):
    """Return n numbers from tribonacci sequence with a given signature"""
    seq = signature.copy()
    for i in range(len(seq), n):
        seq.append(seq[i - 3] + seq[i - 2] + seq[i - 1])
    return seq[:n]


print(tribonacci([0, 1, 2], 10))
print(tribonacci([1, 1, 1], 2))
