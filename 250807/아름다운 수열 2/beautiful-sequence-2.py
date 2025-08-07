n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_b.sort()
count = 0

for i in range(n - m + 1):
    new_arr = arr_a[i:i+m]
    new_arr.sort()
    if new_arr == arr_b:
        count += 1

print(count)