import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
MAX_N = 100
# Please write your code here.

ans = sys.maxsize

def count_max_values(x0, y0):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for x, y in points:
        if x > x0 and y > y0:
            count1 += 1
        elif x < x0 and y > y0:
            count2 += 1
        elif x < x0 and y < y0:
            count3 += 1
        else:
            count4 += 1
    
    return max(count1, max(count2, max(count3, count4)))

for i in range(0, MAX_N + 1, 2):
    for j in range(0, MAX_N + 1, 2):
        min_num = count_max_values(i, j)
        ans = min(ans, min_num)

print(ans)