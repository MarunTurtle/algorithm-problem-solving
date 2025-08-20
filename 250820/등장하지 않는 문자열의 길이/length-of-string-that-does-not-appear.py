n = int(input())
letters = input()

ans = n

for m in range(1, n + 1):
    alone = True
    for j in range(0, n-m+1):
        sub = letters[j:j+m]
        for k in range(j + 1, n - m + 1):
            if sub == letters[k: k+m]:
                alone = False
                break
        if not alone: 
            break
    if alone:
        ans = m
        break

print(ans)
