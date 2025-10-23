n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments.sort(key=lambda x : (x[1], x[0]))

ans = 0
path = []

# def overlapped(seg1, seg2):
#     (ax1, ax2), (bx1, bx2) = seg1, seg2
#     return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or
#            (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)

# def possible():
#     for i, seg1 in enumerate(path):
#         for j, seg2 in enumerate(path):
#             if i < j and overlapped(seg1, seg2):
#                 return False
#     return True

def backtrack(depth, last_end):
    global ans

    if depth == n:
        ans = max(ans, len(path))
        return
    
    s, e = segments[depth]
    
    if s > last_end:
        path.append(segments[depth])
        backtrack(depth + 1, e)
        path.pop()
    
    backtrack(depth + 1, last_end)

backtrack(0, -1)
print(ans)