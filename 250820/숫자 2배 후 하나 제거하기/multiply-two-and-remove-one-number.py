import sys
INT_MAX = sys.maxsize

n = int(input().strip())
a = list(map(int, input().split()))

# 기본 인접합 S0 = sum |a[k] - a[k+1]|
def edge_val(u, v, doubled_idx):
    if u < 0 or v < 0 or u >= n or v >= n:
        return 0
    x = a[u]*2 if u == doubled_idx else a[u]
    y = a[v]*2 if v == doubled_idx else a[v]
    return abs(x - y)

# 기본 인접합
S0 = sum(abs(a[k] - a[k+1]) for k in range(n-1))

ans = INT_MAX

for i in range(n):  # i: 2배할 위치
    # S0' = "i를 2배한 뒤"의 인접합 (두 간선만 수정)
    S0_prime = S0
    # 빼고
    if i-1 >= 0: S0_prime -= abs(a[i-1] - a[i])
    if i+1 <  n: S0_prime -= abs(a[i]   - a[i+1])
    # 더한다 (2배 반영)
    if i-1 >= 0: S0_prime += abs(a[i-1] - 2*a[i])
    if i+1 <  n: S0_prime += abs(2*a[i] - a[i+1])

    for j in range(n):  # j: 제거할 위치
        # 제거는 (j-1, j), (j, j+1) 제거 + (j-1, j+1) 생성
        res = S0_prime
        res -= edge_val(j-1, j, i)
        res -= edge_val(j, j+1, i)
        res += edge_val(j-1, j+1, i)
        ans = min(ans, res)

print(ans)