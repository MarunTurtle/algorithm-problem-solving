n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

j = n - 1
for i in range(n - 1, -1, -1):
    if a[i] == b[j]:
        j -= 1
print(j + 1)  # 최소 이동 횟수
