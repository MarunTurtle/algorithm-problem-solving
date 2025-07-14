# even number
# reverse order

n = int(input())

nums = list(map(int, input().split()))
nums = nums[::-1]

for num in nums:
    if num % 2 == 0:
        print(num, end=" ")
