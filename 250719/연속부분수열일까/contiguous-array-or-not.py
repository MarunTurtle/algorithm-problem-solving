n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

is_part = False

for i in range(n - m):
    if a[i:i+m] == b:
        is_part = True
        break

if is_part:
    print('Yes')
else:
    print('No')

