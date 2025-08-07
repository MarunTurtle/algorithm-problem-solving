n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i, n):
        total_sum = 0
        for k in range(i, j+1):
            total_sum += arr[k]
        length = j + 1 - i
        if total_sum % length == 0:
            avg = total_sum // length  # 정수 평균
            if avg in arr:
                count += 1

print(count)