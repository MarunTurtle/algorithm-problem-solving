n = int(input())
arr = list(input().split())
arr_number = [ord(c) for c in arr]
count = 0
for i in range(n-1):
    for j in range(i, n):
        if arr_number[i] > arr_number[j]:
            count += 1

print(count)