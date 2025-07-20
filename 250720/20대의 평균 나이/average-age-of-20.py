ans = 0
cnt = 0

while True:
    n = int(input())
    cnt += 1
    if 20 <= ans <= 29:
        ans += n
    else:
        print(f"{(ans // cnt):.1f}")
        break