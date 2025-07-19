n = int(input())

cnt = 1

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n - i):
        print(cnt, end=" ")
        if cnt == 9:
            cnt = 1
        else:
            cnt += 1
    print()