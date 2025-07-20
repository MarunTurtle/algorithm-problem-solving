cnt = 0

for _ in range(5):
    n = int(input())
    cnt += 1
    if n % 3 == 0:
        if cnt == 5:
            print(1)
        else:
            continue
    else:
        print(0)
        break