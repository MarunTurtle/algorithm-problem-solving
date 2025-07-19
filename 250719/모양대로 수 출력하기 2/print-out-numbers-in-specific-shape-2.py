n = int(input())

cnt = 0

for i in range(n):
    for j in range(n):
        print(f"{2 * (cnt + 1)}", end=" ")
        if cnt == 3:
            cnt = 0
        else:
            cnt += 1
    print()