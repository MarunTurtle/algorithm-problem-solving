patterns = list(input())
n = len(patterns)

cnt = 0

for i in range(n-1):
    if patterns[i] == ')':
        continue
    for j in range(i+1, n):
        if patterns[j] == '(':
            continue
        else:
            # print(i, j)
            cnt += 1

print(cnt)
