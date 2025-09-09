n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = [0] + arr
count = 0
covered_end = 0

i = 1
while i <= n:
    if arr[i] == 1 and i > covered_end:
        p = min(n, i + m)
        count += 1
        covered_end = p + m
        i = covered_end + 1
    else:
        i += 1

print(count)