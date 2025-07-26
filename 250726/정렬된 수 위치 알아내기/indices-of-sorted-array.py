n = int(input())
nums = list(map(int, input().split()))

indexed_nums = [(i, num) for i, num in enumerate(nums)]

indexed_nums.sort(key = lambda x:x[1])

ranks = [0] * n

for rank, (i, _)  in enumerate(indexed_nums):
    ranks[i] = rank + 1

print(*ranks)