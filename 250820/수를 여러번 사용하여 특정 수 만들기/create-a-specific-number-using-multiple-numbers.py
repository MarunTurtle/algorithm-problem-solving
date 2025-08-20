A, B, C = map(int, input().split())
ans = 0
for i in range(C // A + 1):
    for j in range(C // B + 1):
        s = i*A + j*B
        if s <= C:
            ans = max(ans, s)
print(ans)
