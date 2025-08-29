n = int(input())
before = [0] + list(map(int, input().split()))
after = [0] + list(map(int, input().split()))
need = [after[i] - before[i] for i in range(n+1)]

ans = 0

for i in range(n, 0, -1):
    if need[i] > 0:
        need_to_move = need[i]
        for j in range(i-1, 0, -1):
            if need_to_move == 0:
                break
            if need[j] < 0:
                moving = min(need_to_move, before[j])
                need_to_move -= moving
                need[j] += moving
                ans += moving * (i - j)
        need[i] = need_to_move
    
print(ans)
        