n = int(input())

ans = [[0 for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(r + 1):
        if c == 0 or c == r:
            ans[r][c] = 1
            print(f"{ans[r][c]}", end=" ")
        else:
            ans[r][c] = ans[r-1][c] + ans[r-1][c-1]
            print(f"{ans[r][c]}", end=" ")
    print()