n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
path = []

def get_xor(path):
    res = path[0]
    for i in range(1, len(path)):
        res ^= path[i]
    return res


def get_max_num(cur_num, cnt):
    global ans
    if cur_num == n:
        if cnt == m:
            value = get_xor(path)
            ans = max(ans, value)
        return
    
    path.append(A[cur_num])
    get_max_num(cur_num + 1, cnt + 1)
    path.pop()

    get_max_num(cur_num + 1, cnt)

get_max_num(0, 0)
print(ans)
