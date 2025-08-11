import sys
input = sys.stdin.readline

level = list(map(int, input().split()))  # 6개
ans = 10**18
idx_all = list(range(6))

# 첫 쌍은 항상 (0, j)로 고정해 중복 제거
for j in range(1, 6):
    s1 = level[0] + level[j]
    rem = [x for x in idx_all if x not in (0, j)]  # 남은 4명 (오름차순)

    # 남은 4명 중 가장 작은 rem[0]을 두 번째 쌍의 앵커로 고정
    for t in range(1, 4):
        a, b = rem[0], rem[t]              # 두 번째 쌍
        # 나머지 두 명이 세 번째 쌍
        c, d = [x for x in rem if x not in (a, b)]

        s2 = level[a] + level[b]
        s3 = level[c] + level[d]
        diff = max(s1, s2, s3) - min(s1, s2, s3)
        if diff < ans:
            ans = diff

print(ans)