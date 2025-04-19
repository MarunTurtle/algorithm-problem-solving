from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])
    # 방향 벡터 (상, 하, 좌, 우)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    # 셀(r,c)를 0~n*m-1 인덱스로 변환
    def idx(r, c): return r * m + c

    # 시작·도착 위치 및 초기 마스크 계산
    red_start = blue_start = red_goal = blue_goal = None
    for r in range(n):
        for c in range(m):
            v = maze[r][c]
            if v == 1: red_start = idx(r,c)
            elif v == 2: blue_start = idx(r,c)
            elif v == 3: red_goal  = idx(r,c)
            elif v == 4: blue_goal = idx(r,c)

    # 큐에 (red_pos, blue_pos, red_mask, blue_mask, depth) 저장
    # mask의 비트는 방문한 칸 표시
    start_rmask = 1 << red_start
    start_bmask = 1 << blue_start
    q = deque([(red_start, blue_start, start_rmask, start_bmask, 0)])
    seen = set([(red_start, blue_start, start_rmask, start_bmask)])

    while q:
        rpos, bpos, rmask, bmask, d = q.popleft()
        # 둘 다 도착했으면 깊이 반환
        if rpos == red_goal and bpos == blue_goal:
            return d

        # 다음에 빨강이 선택할 수 있는 후보
        red_moves = []
        if rpos == red_goal:
            red_moves = [red_goal]  # 이미 도착했으면 고정
        else:
            rr, rc = divmod(rpos, m)
            for dr, dc in dirs:
                nr, nc = rr + dr, rc + dc
                ni = idx(nr,nc)
                # 범위, 벽, 이미 방문한 칸 체크
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5:
                    if not (rmask & (1<<ni)):
                        red_moves.append(ni)

        # 파랑 후보
        blue_moves = []
        if bpos == blue_goal:
            blue_moves = [blue_goal]
        else:
            br, bc = divmod(bpos, m)
            for dr, dc in dirs:
                nr, nc = br + dr, bc + dc
                ni = idx(nr,nc)
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5:
                    if not (bmask & (1<<ni)):
                        blue_moves.append(ni)

        # 한 턴에 가능한 모든 (빨강→, 파랑→) 조합
        for nr in red_moves:
            for nb in blue_moves:
                # 같은 칸으로 겹치기 금지
                if nr == nb:
                    continue
                # 서로 자리 바꾸기 금지
                if nr == bpos and nb == rpos:
                    continue

                # 새 마스크
                nrm = rmask | (1<<nr)
                nbm = bmask | (1<<nb)
                state = (nr, nb, nrm, nbm)
                if state in seen:
                    continue
                seen.add(state)
                q.append((nr, nb, nrm, nbm, d+1))

    # 불가능할 경우
    return 0