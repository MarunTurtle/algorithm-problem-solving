n = int(input())
cows = list(map(int, input().split()))

# Please write your code here.
cnt = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cows[i] <= cows[j] and cows[j] <= cows[k]:
                cnt += 1

print(cnt)