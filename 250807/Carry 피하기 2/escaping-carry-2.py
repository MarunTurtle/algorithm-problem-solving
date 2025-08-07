import sys

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

max_ans = -sys.maxsize

def does_not_carry(num1, num2):
    n, m = num1, num2
    min_len = min(len(str(n)), len(str(m)))

    for i in range(min_len):
        if n%10 + m%10 >= 10:
            return False
        else:
            n //= 10
            m //= 10
    return True

for i in range(n-2):
    for j in range(i+1, n-1):
        if does_not_carry(nums[i], nums[j]):
            sum_nums = nums[i] + nums[j]
            for k in range(j+1, n):
                if does_not_carry(sum_nums, nums[k]):
                    ans = sum_nums + nums[k]
                    max_ans = max(max_ans, ans)

print(max_ans)