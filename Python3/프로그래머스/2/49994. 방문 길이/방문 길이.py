def solution(dirs):
    
    # 방향 선언
    move_map = {'U': (0, 1),  'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    
    # (0, 0)에서 출발
    x, y = 0, 0
    
    # 이동 경로 저장할 배열 선언
    visited = set()
    
    # 모든 방향마다 이동 수행
    for dir in dirs:
        # 이동한 경로를 저장
        dx, dy = move_map[dir]
        nx, ny = x + dx, y + dy
        
        # 경계를 벗어나면 무시
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = ((x, y), (nx, ny)) if (x, y) < (nx, ny) else ((nx, ny), (x, y))            
            visited.add(path)
            x, y = nx, ny
        
    return len(visited)