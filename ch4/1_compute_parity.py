# Compute the parity of a very large number of 64-bit words

# Brute force - iteratively tests the value of each bit while counting 1s.

def compute_parity(x: int) -> int:
    result = 0
    while (x):
        # can store modulo as only care about an even or odd count.
        result ^= x & 1
        x >>= 1
    return result

compute_parity(123456)
