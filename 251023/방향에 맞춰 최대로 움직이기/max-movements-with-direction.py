n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

# Please write your code here.
ans = 0
path = [(r, c)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def get_movable_pos(r, c):
    d = move_dir[r][c]
    v = grid[r][c]
    movable_pos = []

    def is_greater(r, c, nr, nc):
        return grid[r][c] < grid[nr][nc]

    if d == 1:
        for i in range(1, r+1):
            movable_pos.append((r - i, c))
    elif d == 2:
        for i in range(1, min(r+1, n-c)):
            movable_pos.append((r - i, c + i))
    elif d == 3:
        for i in range(1, n - c):
            movable_pos.append((r, c + i))
    elif d == 4:
        for i in range(1, min(n - r, n - c)):
            movable_pos.append((r + i, c + i))
    elif d == 5:
        for i in range(1, n - r):
            movable_pos.append((r + i, c))
    elif d == 6:
        for i in range(1, min(n-r, c+1)):
            movable_pos.append((r + i, c - i))
    elif d == 7:
        for i in range(1, c+1):
            movable_pos.append((r, c - i))
    else:
        for i in range(1, min(r + 1, c + 1)):
            movable_pos.append((r - i, c - i))
        
    final_pos = []

    for pos in movable_pos:
        if is_greater(r, c, pos[0], pos[1]):
            final_pos.append(pos)

    return final_pos 


def backtrack(depth):
    global ans, r, c

    ans = max(ans, len(path)-1)

    if depth == n*n:
        return
    
    r, c = path[-1]

    movable_pos = get_movable_pos(r, c)

    for pos in movable_pos:
        path.append(pos)
        backtrack(depth + 1)
        path.pop()


backtrack(0)
print(ans)