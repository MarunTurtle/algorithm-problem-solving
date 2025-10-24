import sys
INT_MAX = sys.maxsize

n = int(input())
grid = [list(input()) for _ in range(n)]
start = (0, 0)
end = (0, 0)
coins = []
ans = INT_MAX

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i, j)
        elif grid[i][j] != '.':
            grid[i][j] = int(grid[i][j])
            coins.append((grid[i][j], (i, j)))

coins.sort(key = lambda x : x[0])

def get_dist(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return abs(r1 - r2) + abs(c1 - c2)

def get_min_route(idx, dist, coin_cnt, last_coin_pos):
    global ans
    
    if coin_cnt == 3:
        tmp = dist + get_dist(last_coin_pos, end)
        if ans > tmp:
            ans = tmp
        return

    if idx >= len(coins) or coin_cnt + (len(coins) - idx) < 3:
        return
    
    dist += get_dist(last_coin_pos, coins[idx][1])  
    get_min_route(idx + 1, dist, coin_cnt + 1, coins[idx][1])
    
    dist -= get_dist(last_coin_pos, coins[idx][1])
    get_min_route(idx + 1, dist, coin_cnt, last_coin_pos)
    
if len(coins) < 3:
    ans = -1
else:
    get_min_route(0, 0, 0, start)

print(ans)