a, b = map(int, input().split())

nums = []

for m in range(b, a - 1, -1):
        if m % 2 == 1:
            continue
        else:
            nums.append(m)           

for i in range(1, 10):
    print(' / '.join(f"{m} * {i} = {m*i}" for m in nums))
