k, n = map(int, input().split())

ans = []

def choose(curr_num):
    if curr_num == n + 1:
        print(*ans)
        return
    
    for i in range(1, k+1):
        ans.append(i)
        choose(curr_num+1)
        ans.pop()
    return 

choose(1)