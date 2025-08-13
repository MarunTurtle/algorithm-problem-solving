n = int(input())
a = list(map(int, input().split()))

ans = 0

# Please write your code here.
for k in range(1, max(a)): # k의 수 완탐
    count = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if k == a[i] or k == a[j]:
                continue
            if (a[i] < k and k < a[j]) or (a[i] > k and k > a[j]):
                if abs(a[i] - k) == abs(k - a[j]):
                    count += 1
    ans = max(ans, count)

print(ans)