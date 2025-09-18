import sys
from itertools import permutations

input = sys.stdin.readline

N, M, K = map(int, input().split())
A0 = [[0]*(M+1)]
for _ in range(N):
    A0.append([0] + list(map(int, input().split())))

ops = [tuple(map(int, input().split())) for _ in range(K)]

def rotate_once(a, r, c, s):
    for t in range(1, s+1):
        top, left  = r - t, c - t
        bottom, right = r + t, c + t

        path = []
        for col in range(left, right):
            path.append((top, col))
        for row in range(top, bottom):
            path.append((row, right))
        for col in range(right, left, -1):
            path.append((bottom, col))
        for row in range(bottom, top, -1):
            path.append((row, left))

        last_val = a[path[-1][0]][path[-1][1]]
        for i in range(len(path)-1, 0, -1):
            r0, c0 = path[i]
            r1, c1 = path[i-1]
            a[r0][c0] = a[r1][c1]
        r0, c0 = path[0]
        a[r0][c0] = last_val

def value_of(a):
    ans = float('inf')
    for r in range(1, N+1):
        ans = min(ans, sum(a[r][1:M+1]))
    return ans

answer = float('inf')

for order in permutations(ops, K):
    a = [row[:] for row in A0]
    for (r, c, s) in order:
        rotate_once(a, r, c, s)
    answer = min(answer, value_of(a))

print(answer)
