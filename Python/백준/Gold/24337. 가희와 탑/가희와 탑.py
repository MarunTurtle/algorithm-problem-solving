import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

if N < a + b - 1:
    print(-1)
    sys.exit(0)

M = max(a, b)
extra = N - (a + b - 1)
ans = []

if a == 1 and b == 1:
    ans = [1] * N

elif a == 1:
    ans.append(M)
    ans += [1] * extra
    ans += list(range(b - 1, 0, -1))

elif b == 1:
    ans += [1] * (extra + 1)  
    if a >= 2:
        ans += list(range(2, a))  
    ans.append(M)

else:
    ans += [1] * (extra + 1)     
    if a >= 2:
        ans += list(range(2, a))  
    ans.append(M)                 
    ans += list(range(b - 1, 0, -1))

print(*ans)
