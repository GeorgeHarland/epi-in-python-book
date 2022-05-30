# Differently optimised to count the number of bits that are set to 1 in a nonnegative integer.

# For each digit: +1 to count if bit is 1, then move to the right bit until no more bits
# Starts with the least-significant bit
# Time complexity is O(n), where n is the number of bits used to represent the integer
def count_bits_start(x: int) -> int:
    num_bits = 0
    while (x):
        num_bits += x & 1
        x = x >> 1
    return num_bits
print(count_bits_start(47))