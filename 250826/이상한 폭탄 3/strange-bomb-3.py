n, k = tuple(map(int, input().split()))
bombs = [int(input()) for _ in range(n)]

bomb_num = 0
bomb_cnt = 0
bomb_exploded = [0] * n

def explode(x, bomb_exploded):
    if x == n-1:
        return bomb_exploded
    bomb_num = bombs[x]
    for i in range(x+1, n):
        if bomb_exploded[i] == 0 and bombs[i] == bomb_num and i - x <= k:
            bomb_exploded[x] = 1
            bomb_exploded[i] = 1
            bomb_exploded = explode(i, bomb_exploded)
    return bomb_exploded

for i in range(n):
    bomb_exploded = explode(i, bomb_exploded)
    cur_bomb_cnt = 0

    for j in range(n):
        if bomb_exploded[j] == 1 and bombs[j] == bombs[i]:
            cur_bomb_cnt += 1

    if cur_bomb_cnt > bomb_cnt:
        bomb_num = bombs[i]
        bomb_cnt = cur_bomb_cnt
    # print(bomb_exploded)

print(bomb_num)