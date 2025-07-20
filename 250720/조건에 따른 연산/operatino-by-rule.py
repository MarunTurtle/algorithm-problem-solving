n = int(input())
cnt = 0

def func(n):
    if n % 2 == 0:
        n = n * 3 + 1
    else:
        n = n * 2 + 2
    return n

while n < 1000:
    n = func(n)
    cnt += 1

print(cnt)