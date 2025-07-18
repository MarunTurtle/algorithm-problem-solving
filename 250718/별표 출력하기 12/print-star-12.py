n = int(input())

arr_2d = [[' ' for _ in range(n)] for _ in range(n)]

for j in range(n):
    arr_2d[0][j] = '*'

for j in range(n):
    for i in range(n):
        if j%2==1 and i<=j:
            arr_2d[i][j] = '*'

for i in arr_2d:
    print(*i)