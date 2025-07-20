n = int(input())
d = 1
cnt = 0

while True:
    n = n // d
    cnt += 1
    d += 1
    if n <= 1:
        print(cnt)
        break