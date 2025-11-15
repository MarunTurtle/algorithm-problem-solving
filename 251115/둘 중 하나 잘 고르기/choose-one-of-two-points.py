n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

dp = [[-1, -1, -1] for _ in range(2 * n + 1)]
print(dp)
