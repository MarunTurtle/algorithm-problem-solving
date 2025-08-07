MAX_NUM = 100

n, k = map(int, input().split())
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    candies, idx = map(int, input().split())