patterns = list(input())
n = len(patterns)
cnt = 0

for i in range(n-3):
    if patterns[i] == '(' and patterns[i+1] == '(':
        for k in range(i+2, n-1):
            if patterns[k] == ')' and patterns[k+1] == ')':
                # print(i, i+1, k, k+1)
                cnt += 1

print(cnt)