import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if len(data) < 2:
    sys.exit(0)

n, m = data[0], data[1]
heights = data[2:2+n]
if not heights:
    print(0)
    sys.exit(0)

low, high = 0, max(heights)
answer = 0

while low <= high:
    mid = (low + high) // 2

    total = 0
    for h in heights:
        if h > mid:
            total += h - mid
            if total >= m:  # 조기 종료(미세 최적화)
                break

    if total >= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)