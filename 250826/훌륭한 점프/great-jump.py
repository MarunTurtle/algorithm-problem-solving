import sys
import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))
n, k = map(int, input().split())
arr = list(map(int, input().split()))



def is_possible(a):
    picked = [-k] + [i for i, x in enumerate(arr) if x <= a] + [n - 1]
    for i in range(1, len(picked)):
        if picked[i] - picked[i - 1] > k:
            return False
    return True

for a in range(1, max(arr) + 1):
    if is_possible(a):
        print(a)
        break