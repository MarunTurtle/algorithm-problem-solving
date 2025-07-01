import sys
input = sys.stdin.readline
print = sys.stdout.write

N, Q = map(int, input().split())
A = sorted(map(int, input().split()))

# 누적합 배열 생성
prefix = [0]
for num in A:
    prefix.append(prefix[-1] + num)

for _ in range(Q):
    L, R = map(int, input().split())
    print(str(prefix[R] - prefix[L-1]) + '\n')
