import sys

n = int(input())
seats = list(map(int, list(input())))
pos_ones = [i for i, c in enumerate(seats) if c == 1]

def get_minimum_dist(at):
    arr = pos_ones + [at]
    arr.sort()
    return min(arr[i+1] - arr[i] for i in range(len(arr) - 1))

ans = -1
for i in range(n):
    if seats[i] == 0:
        ans = max(ans, get_minimum_dist(i))

print(ans)

