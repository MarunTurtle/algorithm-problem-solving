k, n = map(int, input().split())
ans = []

def get_permutation(curr_num):
    if curr_num == n:
        print(*ans)
        return
    
    for i in range(1, k+1):
        ans.append(i)
        get_permutation(curr_num+1)
        ans.pop()

get_permutation(0)