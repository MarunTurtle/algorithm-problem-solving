import sys
INT_MAX = sys.maxsize

n = int(input())
num = list(map(int, input().split()))

ans = INT_MAX
total_sum = sum(num)

def get_combination_diff(idx, cnt, curr_sum):
    global ans
    if cnt == n:
        ans = min(ans, abs(total_sum - (curr_sum * 2)))
        return

    if idx == 2*n:
        return

    get_combination_diff(idx + 1, cnt + 1, curr_sum + num[idx])
    get_combination_diff(idx + 1, cnt, curr_sum)

get_combination_diff(0, 0, 0)
print(ans)