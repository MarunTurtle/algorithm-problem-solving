n, k = tuple(map(int, input().split()))
stage = [0] * (n + 1)

for i in range(k):
    a, b = tuple(map(int, input().split()))
    for j in range(a, b+1):
        stage[j] += 1

print(max(stage))