n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)] 

cnt = 1

for start_r in range(n):
    for start_c in range(m):
        if matrix[start_r][start_c] == 0:
            curr_r = start_r
            curr_c = start_c
        
        while 0 <= curr_c and curr_r < n:
            matrix[curr_r][curr_c] = cnt
            
            curr_r += 1
            curr_c -= 1
            cnt += 1

for row in matrix:
    print(*row)