def solution(n, computers):
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count
