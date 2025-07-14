n = int(input())
nums = [x**2 for x in list(map(int, input().split()))]

for num in nums:
    print(num, end=" ")