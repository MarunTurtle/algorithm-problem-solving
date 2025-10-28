n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [list() for _ in range(n + 1)]
visited = [False] * (n+1)

for edge in edges:
    s, e = edge
    graph[s].append(e)
    graph[e].append(s)

def dfs(x):
    for vertex in graph[x]:
        if not visited[vertex]:
            visited[vertex] = True
            dfs(vertex)

visited[1] = True
dfs(1)
print(sum(1 for v in visited if v) - 1)