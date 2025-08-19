n = int(input())
arr = list(map(int, input().split()))

INF = 10**18
ans = INF

for d in range(n):          # 2배할 위치
    for r in range(n):      # 제거할 위치
        b = arr[:]          # 원본 복사
        b[d] *= 2           # 먼저 2배
        b.pop(r)            # 그 다음 하나 제거

        # 인접 차이의 합 계산
        s = 0
        for i in range(len(b) - 1):
            s += abs(b[i] - b[i+1])
        ans = min(ans, s)

print(ans)