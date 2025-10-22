n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments.sort(key=lambda x: (x[1], x[0]))

max_cnt = 0
def backtrack(depth, last_end, path):
    global max_cnt
    if depth == n:
        max_cnt = max(max_cnt, len(path))
        return
    
    s, e = segments[depth]
    if s > last_end:
        path.append(segments[depth])
        backtrack(depth + 1, e, path)
        path.pop()
    backtrack(depth + 1, last_end, path)

backtrack(0, -1, [])

print(max_cnt)