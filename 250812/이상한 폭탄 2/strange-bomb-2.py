n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

# Please write your code here.

max_num = -1

for i in range(n-1):
    for j in range(i+1, n):
        if num[i] == num[j]:
            if abs(i - j) <= k:
                max_num = max(max_num, num[i])

print(max_num)
