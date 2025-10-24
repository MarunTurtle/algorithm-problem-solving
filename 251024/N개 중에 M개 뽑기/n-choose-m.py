# n이하 숫자, M개 선택
n, m = map(int, input().split())

comb = []

def get_combination(depth, start):
    if depth == m:
        print(*comb)
    
    for v in range(start+1, n+1):
        comb.append(v)
        get_combination(depth+1, v)
        comb.pop()

get_combination(0, 0)