n = int(input())
max_cnt = 0
cnt = 0
curr = 0
# 매번 숫자를 읽음
for i in range(n):
    new_num = int(input())
    # 첫 숫자일 경우 (cnt = 0) 또는 다른 숫자일 경우
    if cnt == 0 or curr != new_num:
        max_cnt = max(cnt, max_cnt)
        cnt = 1
        curr = new_num
    else:
        cnt += 1
        if i == n-1:
            max_cnt = max(cnt, max_cnt)

print(max_cnt)

