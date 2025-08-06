import sys
MIN_MOV = sys.maxsize

n = int(input())
room_capacity = [int(input()) for _ in range(n)]
ans = MIN_MOV
people = sum(room_capacity)

for i in range(n):      # 모든 방을 시작점으로
    cur_mov = 0     
    cur_people = people
    for j in range(n):  # 해당 방을 시작점으로 한 바퀴 돌기
        cur_idx = (i + j) % n
        cur_mov += room_capacity[cur_idx] * j
        cur_people -= room_capacity[cur_idx]
    
    ans = min(ans, cur_mov)

print(ans)