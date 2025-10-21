from collections import deque

n, m = map(int, input().split())
grid = []
for i in range(n):
    nums = list(map(int, input().split()))
    row = []
    for j in range(n):
        row.append([nums[j]])
    grid.append(row)

move_nums = list(map(int, input().split()))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def move(r, c, s, max_value_pos):
    nr, nc = max_value_pos
    tmp = grid[r][c][s:]
    grid[r][c] = grid[r][c][:s]
    grid[nr][nc].extend(tmp)

def simulate(num):
    r, c, s = find(num)
    # print(find(num))
    max_value = -1
    max_value_pos = (-1, -1)
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if in_range(nr, nc):
            nums = grid[nr][nc]
            if len(nums) != 0:
                for elem in nums:
                    max_value = max(max_value, elem)
                    if max_value == elem:
                        max_value_pos = (nr, nc)
    if max_value_pos == (-1, -1):
        return
    move(r, c, s, max_value_pos)

def find(num):
    for r in range(n):
        for c in range(n):
            for s in range(len(grid[r][c])):
                if num == grid[r][c][s]:
                    return (r, c, s)


for number in move_nums:
    simulate(number)

for row in grid:
    for nums in row:
        if len(nums) == 0:
            print("None")
        else:
            for i in range(len(nums)-1, -1, -1):
                print(nums[i], end=" ")
            print("")

