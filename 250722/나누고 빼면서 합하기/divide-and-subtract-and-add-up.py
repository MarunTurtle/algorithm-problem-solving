n, m = map(int, input().split())
a = list(map(int, input().split()))

def modify():
    global m
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1

total = 0

while m >= 1:
    total += a[m-1]
    modify()

print(total)