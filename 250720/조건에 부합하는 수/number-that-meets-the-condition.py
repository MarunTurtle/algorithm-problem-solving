n = int(input())

for i in range(1, n+1):
    a = i // 8
    if not (i % 2 == 0 and i % 4 != 0):
        if not a % 2 == 0:
            if not i % 7 < 4:
                print(i, end=" ")
            else:
                continue
        else:
            continue
    else:
        continue
    