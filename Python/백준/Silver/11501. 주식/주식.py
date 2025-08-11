import sys

it = map(int, sys.stdin.buffer.read().split())
t = next(it)
out = []
for _ in range(t):
    n = next(it)
    prices = [next(it) for _ in range(n)]

    mx = 0
    profit = 0  # 64-bit 범위 내
    for p in reversed(prices):
        if p > mx:
            mx = p
        else:
            profit += mx - p
    out.append(str(profit))

print("\n".join(out))
