matrix = [[0] * 4 for _ in range(4)]

for i in range(4):
    nums = list(map(int, input().split()))
    for j in range(4):
        matrix[i][j] = nums[j]

total = 0

for i in range(4):
    for j in range(i+1):
        total += matrix[i][j]

print(total)