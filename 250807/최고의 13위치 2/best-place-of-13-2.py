# 변수 선언 및 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# Step 1.
# 첫 번째 격자를 놓습니다. (i , j)
max_cnt = 0
for i in range(n):
    # 격자를 벗어나지 않을 범위로만 잡습니다.
    for j in range(n - 2):
        # 두 번째 격자를 놓습니다. (k , l)
        for k in range(n):
            # 격자를 벗어나지 않을 범위로만 잡습니다.
            for l in range(n - 2):
                # Step2. 두 격자가 겹치는 경우에는 가짓수로 세지 않습니다.
                if i == k and abs(j - l) <= 2:
                        continue
                
                # Step 3. 두 격자가 겹치지 않는 경우에 대해 동전 수를 세어 갱신해줍니다.
                cnt1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                cnt2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)
