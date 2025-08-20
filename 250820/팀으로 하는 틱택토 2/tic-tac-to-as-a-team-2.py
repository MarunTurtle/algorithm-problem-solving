grid = [list(input()) for _ in range(3)]

count = 0
couple = []

for i in range(3):
    nums = set(grid[i])
    if len(nums) == 2:
        if nums not in couple:
            count += 1
            couple.append(nums)


for i in range(3):
    nums = []
    for j in range(3):
        nums.append(grid[j][i])
    if len(set(nums)) == 2:
        if set(nums) not in couple:
            count += 1
            couple.append(set(nums))


num_set1 = []
for i in range(3):
    for j in range(3):
        if i == j:
            num_set1.append(grid[i][j])

if len(set(num_set1)) == 2:
    if set(num_set1) not in couple:
        count += 1
        couple.append(set(num_set1))

num_set2 = []   
for i in range(3):
    for j in range(3):
        if i == 2 - j:
            num_set2.append(grid[i][j])

if len(set(num_set2)) == 2:
    if set(num_set2) not in couple:
        count += 1
        couple.append(set(num_set2))

# print(couple)
print(count)

