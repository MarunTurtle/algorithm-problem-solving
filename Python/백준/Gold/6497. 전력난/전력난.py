import sys
input = sys.stdin.readline

def find(p, x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def union(p, r, a, b):
    ra, rb = find(p, a), find(p, b)
    if ra == rb:
        return False
    if r[ra] < r[rb]:
        ra, rb = rb, ra
    p[rb] = ra
    if r[ra] == r[rb]:
        r[ra] += 1
    return True

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    edges = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total += z

    edges.sort() 
    parent = list(range(m))
    rank = [0] * m

    mst = 0
    picked = 0
    for cost, a, b in edges:
        if union(parent, rank, a, b):
            mst += cost
            picked += 1
            if picked == m - 1:
                break

    print(total - mst)
