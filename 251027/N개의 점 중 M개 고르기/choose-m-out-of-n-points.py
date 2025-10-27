import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

selected = []
ans = INT_MAX

def get_uklid(pairs):
    r, c = pairs[0]
    nr, nc = pairs[1]

    return (r - nr)**2 + (c - nc)**2

def calc(selected):
    max_ans = 0
    for i in range(m):
        for j in range(i + 1, m):
            max_ans = max(max_ans, get_uklid([selected[i], selected[j]]))

    return max_ans

def get_min_diff_btw_furthest(depth, cur_idx):
    global ans
    if depth == m:
        cand = calc(selected)
        ans = min(ans, cand)
        return
    
    if cur_idx == n:
        return    

    selected.append(points[cur_idx])
    get_min_diff_btw_furthest(depth + 1, cur_idx + 1)
    selected.pop()
    get_min_diff_btw_furthest(depth, cur_idx + 1)

get_min_diff_btw_furthest(0, 0)
print(ans)