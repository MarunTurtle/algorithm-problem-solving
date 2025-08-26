import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(a):
    picked = [i for i, x in enumerate(arr) if x <= a]
    for i in range(1, len(picked)):
        if picked[i] - picked[i - 1] > k:
            return False
    return True

for a in range(arr[0], max(arr)+1):
    if is_possible(a):
        print(a)
        break
