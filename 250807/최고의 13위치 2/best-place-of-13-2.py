import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = -sys.maxsize

# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def count_coins(x, y):
    cnt = 0
    for i in range(3):
        nx, ny = x, y + i
        if not in_range(nx, ny):
            return 0
        if grid[nx][ny] == 1:
            cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        temp_ans = count_coins(i, j)

        for k in range(i, n):
            if k == i:
                for l in range(j+3, n):
                    temp_ans += count_coins(k, l)    
                    print(i, j, k, l)
                    ans = max(ans, temp_ans)
                    temp_ans = count_coins(i, j)
            else:
                for l in range(n):
                    temp_ans += count_coins(k, l)    
                    print(i, j, k, l)
                    ans = max(ans, temp_ans)
                    temp_ans = count_coins(i, j)

            
print(ans)