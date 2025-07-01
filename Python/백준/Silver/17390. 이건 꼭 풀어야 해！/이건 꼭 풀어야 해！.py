import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

# 누적합 배열 생성
prefix = [0]
for num in A:
    prefix.append(prefix[-1] + num)

for _ in range(Q):
    L, R = map(int, input().split())
    print(prefix[R] - prefix[L-1])