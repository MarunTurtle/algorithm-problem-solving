n = int(input())
letters = input()

ans = n // 2 + 1

for i in range(n//2, 0, -1):
    chunk = letters[:i]
    m = len(chunk)
    # print(chunk)
    alone = True

    for j in range(m, n-m+1):
        if chunk == letters[j: j+m]:
            # print(chunk, letters[j:j+m])
            alone = False
    
    if alone: 
        ans = min(ans, m)

print(ans)
