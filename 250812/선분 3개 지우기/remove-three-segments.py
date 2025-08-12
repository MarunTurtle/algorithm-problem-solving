n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            grid = [0] * (100+1)
            is_seperate = True
            for l in range(n):
                if l == i or l == j or l == k:
                    continue
                else:
                    for m in range(lines[l][0], lines[l][1] + 1):
                        if grid[m] == 1:
                            is_seperate = False
                        else:
                            grid[m] += 1
            if is_seperate:
                count += 1


print(count)