import sys, math
INT_MAX = sys.maxsize

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

selected = []
ans = INT_MAX

def get_uklid(pairs):
    r, c = pairs[0]
    nr, nc = pairs[1]

    return math.sqrt((r - nr)**2 + (c - nc)**2)

def calc(selected):
    max_ans = 0
    pair = []

    def get_pair_distance(depth, cur_idx):
        nonlocal max_ans
        if depth == 2:
            pos_ans = get_uklid(pair)
            max_ans = max(max_ans, pos_ans)
            return
        if cur_idx == m:
            return

        pair.append(selected[cur_idx])
        get_pair_distance(depth + 1, cur_idx + 1)
        pair.pop()
        get_pair_distance(depth, cur_idx + 1)
    
    get_pair_distance(0, 0)
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
print(round(ans**2))