import sys

n = int(input())
seats = list(input())
ans = 0

def get_min_distance(x):
    min_dist = n
    for i in range(n):
        if i == x:
            continue
        if seats[i] == '1':
            dis = abs(i - x)
            min_dist = min(dis, min_dist)
    return min_dist

for i in range(n):
    if seats[i] == '1':
        continue
    
    # print(f"{i}번째")
    dist = get_min_distance(i)
    ans = max(dist, ans)

print(ans)
