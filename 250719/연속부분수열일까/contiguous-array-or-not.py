n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

is_part = False

if n >= m:
    for i in range(n - m + 1):
        if a[i:i+m] == b:
            is_part = True
            break

if is_part:
    print('Yes')
else:
    print('No')