n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

def get_max_num(cur_idx, cnt, value):
    global ans

    if cnt == m:
        ans = max(ans, value)
        return

    get_max_num(cur_idx + 1, cnt + 1, value ^ A[cur_idx])
    get_max_num(cur_idx + 1, cnt, value)

get_max_num(0, 0, 0)
print(ans)
