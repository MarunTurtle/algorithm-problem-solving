n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = 0

for start in range(1, n+1):
    total = 0
    cur_loc = start
    for moves in range(m):
        total += arr[cur_loc]
        cur_loc = arr[cur_loc]
    ans = max(ans, total)

print(ans)