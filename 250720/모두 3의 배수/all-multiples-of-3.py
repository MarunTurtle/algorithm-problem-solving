cnt = 0

for _ in range(5):
    n = int(input())
    cnt += 1
    if cnt == 5:
        print(1)
        break
    elif n % 3 == 0:
        continue
    else:
        print(0)
        break