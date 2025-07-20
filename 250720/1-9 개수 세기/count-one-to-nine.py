n = int(input())
count = [0]*(10)

nums = list(map(int, input().split()))

for num in nums:
    count[num] += 1

for i in range(1, 10):
    print(count[i])



