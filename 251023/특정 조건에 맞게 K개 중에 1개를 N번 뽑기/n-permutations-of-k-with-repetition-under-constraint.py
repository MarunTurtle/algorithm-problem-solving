K, N = map(int, input().split())

ans = []

def backtrack(depth):
    if depth == N:
        print(*ans)
        return 
    
    for i in range(1, K+1):
        if depth >= 2:
            if ans[depth - 1] == i and ans[depth - 2] == i:
                continue
        ans.append(i)
        backtrack(depth + 1)
        ans.pop()

backtrack(0)
