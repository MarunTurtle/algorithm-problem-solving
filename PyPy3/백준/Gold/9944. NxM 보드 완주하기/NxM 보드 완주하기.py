case = 1

while True:
    try:
        n, m = map(int, input().split())
        grid = [list(map(str, input())) for _ in range(n)]
        starts = []
        to_visit = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == '*':
                    grid[r][c] = 1
                else:
                    grid[r][c] = 0
                    starts.append((r, c))
                    to_visit += 1

        drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]
        # ======

        ans = float('inf')

        def in_range(r, c):
            return 0 <= r < n and 0 <= c < m

        def can_go(r, c, visited):
            return in_range(r, c) and not visited[r][c] and not grid[r][c]

        def visit(r, c, dr, dc, visited):
            a = 0
            marked = 0
            nr, nc = r, c
            while True:
                a += 1
                nr, nc = r + (dr * a), c + (dc * a)
                if can_go(nr, nc, visited):
                    visited[nr][nc] = 1
                    marked += 1
                else:
                    return nr - dr, nc - dc, marked

        def dfs(r, c, steps, visited, visited_cnt):
            global ans

            if visited_cnt == to_visit:
                ans = min(ans, steps)
                return

            if steps >= ans:
                return

            for dr, dc in zip(drs, dcs):
                end_r, end_c, marked = visit(r, c, dr, dc, visited)
                if (end_r, end_c) == (r, c):
                    continue
                dfs(end_r, end_c, steps + 1, visited, visited_cnt + marked)

                for i in range(0, marked):
                    visited[end_r - (dr*i)][end_c - (dc*i)] = 0
                    
        for sr, sc in starts:
            visited = [[0] * m for _ in range(n)]
            visited[sr][sc] = 1
            dfs(sr, sc, 0, visited, 1)

        print(f"Case {case}: {ans if ans != float('inf') else -1}")
        case += 1
    except:
        break