n = int(input())

nums = list(map(str, input().split()))
ans = ""

for num in nums:
    ans += num

l = len(ans)

for i in range(l):
    print(ans[i], end="")
    if (i + 1) % 5 == 0:
        print()

