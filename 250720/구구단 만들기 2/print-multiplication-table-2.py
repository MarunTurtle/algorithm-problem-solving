s, e = map(int, input().split())

for i in range(2, 9, 2):
    print(' / '.join(f"{j} * {i} = {j*i}" for j in range(e, s-1, -1)))
