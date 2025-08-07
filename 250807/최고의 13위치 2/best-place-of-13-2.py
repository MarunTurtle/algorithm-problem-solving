# 입력 받기
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 사전 계산: 3칸짜리 수평선의 합을 저장할 배열
line_sum = [[0] * (n - 2) for _ in range(n)]

# 1. 각 행마다 가능한 3칸짜리 구간의 합을 미리 계산
for i in range(n):
    for j in range(n - 2):
        line_sum[i][j] = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]

# 2. 두 수평선 조합 비교 (겹치지 않도록)
max_cnt = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                # 겹치는 경우 패스
                if i == k and abs(j - l) <= 2:
                    continue
                
                cnt = line_sum[i][j] + line_sum[k][l]
                max_cnt = max(max_cnt, cnt)

print(max_cnt)