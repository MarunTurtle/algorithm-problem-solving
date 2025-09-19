def count_ones_upto(n: int) -> int:
    total = 0
    bit = 0
    while (1 << bit) <= n:
        cycle_len = 1 << (bit + 1)
        full_cycles = (n + 1) // cycle_len
        total += full_cycles * (cycle_len // 2)

        remainder = (n + 1) % cycle_len
        total += max(0, remainder - (cycle_len // 2))
        bit += 1
    return total

A, B = map(int, input().split())
print(count_ones_upto(B) - count_ones_upto(A - 1))
