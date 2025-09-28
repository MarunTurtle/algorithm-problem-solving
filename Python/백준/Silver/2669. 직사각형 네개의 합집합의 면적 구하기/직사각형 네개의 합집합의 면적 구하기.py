squares = [list(map(int, input().split())) for _ in range(4)]
grid = [[False] * 101 for _ in range(101)]
ans = 0

for coords in squares:
    x1, y1, x2, y2, = tuple(coords)
    for x in range(x1, x2):
        for y in range(y1, y2):
            if not grid[x][y]:
                grid[x][y] = True
                ans += 1

print(ans)