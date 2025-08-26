import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(a):

    if arr[0] > a or arr[-1] > a:
        return False

    picked = [i for i, v in enumerate(arr) if v <= a]
    
    if picked[0] != 0 or picked[-1] != n-1:
        return False

    for i in range(1, len(picked)):
        if picked[i] - picked[i - 1] > k:
            return False
    return True

for a in range(max(arr[-1], arr[0]), max(arr)+1):
    if is_possible(a):
        print(a)
        break
