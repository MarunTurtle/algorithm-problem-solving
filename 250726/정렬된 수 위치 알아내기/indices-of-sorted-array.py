n = int(input())
nums = list(map(int, input().split()))
indexed_nums = [(i, nums[i]) for i in range(n)]

indexed_nums.sort(key=lambda x:x[1])

ans = [0]*n

for idx, (i, _) in enumerate(indexed_nums):
    ans[i] = idx + 1

print(*ans)