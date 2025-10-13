n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
def get_sum_1(r, c):
    max_total = 0
    total = 0
    if r + 2 <= n-1:
        for i in range(3):
            total += grid[r+i][c]  
        max_total = max(max_total, total)
    if c + 2 <= m-1:
        for i in range(3):
            total += grid[r][c+i]
        max_total = max(max_total, total)
    return max_total

def get_sum_2(r, c):
    max_total = 0
    if r + 1 <= n-1 and c + 1 <= m-1:
        four_sum = 0
        min_elem = float('inf')
        for i in range(2):
            for j in range(2):
                four_sum += grid[r+i][c+j]
                min_elem = min(min_elem, grid[r+i][c+j])
        max_total = four_sum - min_elem
    return max_total

for r in range(n):
    for c in range(m):
        ans = max(ans, max(get_sum_1(r, c), get_sum_2(r, c)))
        
