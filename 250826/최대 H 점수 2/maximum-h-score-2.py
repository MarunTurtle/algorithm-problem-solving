n, l = tuple(map(int, input().split()))
a = list(map(int, input().split()))
    
# 모든 답을 일일히 가정해 봅니다.
ans = 0
for i in range(1, n + 1):
    # 정답이 i일 때 가능한지 판단합니다.

    # i - 1인 값은 최대 l개까지 i로 올릴 수 있습니다.
    # cnt : i이상인 숫자의 개수(i - 1인 숫자는 l개까지 카운트)
    # cntl : 지금까지 1 증가시킨 숫자의 개수
    cnt = 0
    cntl = 0

    for j in range(n):
        if a[j] >= i:
            cnt += 1
        elif a[j] == i - 1:
            if cntl < l:
                cntl += 1
                cnt += 1

    if cnt >= i:
        ans = i

print(ans)
