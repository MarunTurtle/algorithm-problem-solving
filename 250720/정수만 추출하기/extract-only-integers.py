strings = list(input().split())
nums = ["", ""]

for j in range(len(strings)):
    for i in range(len(strings[j])):
        if not strings[j][i].isdigit():
            break
        else:
            nums[j] += strings[j][i]

ans = 0

for num in nums:
    num = int(num)
    ans += num

print(ans)