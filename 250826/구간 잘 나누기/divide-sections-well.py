
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def can_divide(limit):
    """limit 이하로 구간 합을 유지하며 나눌 수 있는지 검증"""
    cnt = 1  # 구간 개수
    curr_sum = 0

    for num in arr:
        if curr_sum + num > limit:
            cnt += 1
            curr_sum = num
        else:
            curr_sum += num
    return cnt <= m

left = max(arr)        # 최소 가능한 최댓값
right = sum(arr)       # 최대 가능한 최댓값
answer = right

while left <= right:
    mid = (left + right) // 2

    if can_divide(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)