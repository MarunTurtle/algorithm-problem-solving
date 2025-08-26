from collections import Counter
from itertools import combinations

nums = list(map(int, input().split()))
nums.sort()

target = Counter(nums)  # 정답 멀티셋

def build_multiset(a, b, c, d):
    vals = [a, b, c, d,
            a+b, b+c, c+d, d+a,
            a+c, b+d,
            a+b+c, a+b+d, a+c+d, b+c+d,
            a+b+c+d]
    return Counter(vals)

# 마지막 값은 a+b+c+d 여야 함
total = nums[-1]

# 인덱스 0~13 중에서 4개 골라 단일 후보 구성
for i, j, k, l in combinations(range(14), 4):
    a, b, c, d = nums[i], nums[j], nums[k], nums[l]
    if a + b + c + d != total:
        continue
    if build_multiset(a, b, c, d) == target:
        print(a, b, c, d)
        break
