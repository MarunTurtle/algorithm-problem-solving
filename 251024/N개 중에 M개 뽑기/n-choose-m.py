# n이하 숫자, M개 선택
n, m = map(int, input().split())

comb = []

def get_combination(depth, start):
    if depth == m:
        print(*comb)
        return
    
    limit = n - (m - depth) + 1

    for v in range(start+1, limit+1):
        comb.append(v)
        get_combination(depth+1, v)
        comb.pop()

get_combination(0, 0)