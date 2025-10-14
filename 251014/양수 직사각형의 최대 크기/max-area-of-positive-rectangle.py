n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# mask 만들기 양수면 1, 음수면 0
mask = [[1 if grid[i][j] > 0 else 0 for j in range(m)] for i in range(n)]

# 모든 그리드를 보면서 prefix-sum만들기
prefix = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = (
            mask[i-1][j-1]     # 현재 양수 여부 
            + prefix[i][j-1]   # 왼쪽 양수 총 갯수
            + prefix[i-1][j]   # 위쪽 양수 총 갯수
            - prefix[i-1][j-1] # 위,왼 겹치는 양수 갯수 
        )


# 2개의 지점(좌상, 우하)를 잡아서 prefix-sum과 실제 넓이 비교 후 같으면 max-sum 업데이트
max_area = -1

for r1 in range(1, n+1):
    for c1 in range(1, m+1):
        for r2 in range(r1, n + 1):
            for c2 in range(r2, m + 1):
                total = (
                    prefix[r2][c2]                    
                    - prefix[r1-1][c2]
                    - prefix[r2][c1-1]
                    + prefix[r1-1][c1-1]
                )

                area = (r2 - r1 + 1) * (c2 - c1 + 1)

                if total == area:
                    max_area = max(max_area, area)

print(max_area)

