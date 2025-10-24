import sys

INT_MAX = sys.maxsize

# N 격자 크기
n = int(input())
grid = [list(input()) for _ in range(n)]

start = (0, 0)
end = (0, 0)
coins = []

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

# 최소 3개 동전
# S --> E
# 위치를 지나가더라도 동전을 수집하지 않아도 됨
# 동전 수집 시 오름차순으로 수집해야 함
# 같은 위치 2번 이상 지나가는 것 가능

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 3개 수집해서 도착지에 최소 이동
ans = INT_MAX

def get_dist(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return abs(r1 - r2) + abs(c1 - c2)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def get_min_route(idx, dist, coin_cnt, last_coin_pos):
    global ans

    if coin_cnt == 3:
        tmp = dist + get_dist(last_coin_pos, end)
        ans = min(ans, tmp)
    
    if idx == len(coins) or coin_cnt + len(coins) - idx -1 < 3:
        return
    
    dist += get_dist(last_coin_pos, coins[idx+1][1])
    get_min_route(idx + 1, dist, coin_cnt + 1, coins[idx + 1][1])

    dist -= get_dist(last_coin_pos, coins[idx+1][1])
    get_min_route(idx + 1, dist, coin_cnt, coins[idx][1])
    
get_min_route(0, 0, 0, start)
print(ans)