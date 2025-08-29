n = int(input())
before = list(map(int, input().split()))
after = list(map(int, input().split()))

ans = 0

for i in range(n):
    if before[i] > after[i]:
        moving = before[i] - after[i]
        ans += moving
        before[i+1] += moving
        before[i] -= moving

print(ans)