n, low, mid, high = map(int, input().split())
temps = [tuple(map(int, input().split())) for _ in range(n)]

min_temp = 1001
max_temp = 0

for i in range(n):
    for j in range(2):
        min_temp = min(min_temp, temps[i][j])
        max_temp = max(max_temp, temps[i][j])


max_sum = 0

def get_performance(j, temp):
    global low, mid, high

    btm = temps[j][0]
    top = temps[j][1]

    if temp < btm:
        return low
    elif temp > top:
        return high
    else:
        return mid

        
for temp in range(min_temp-1, max_temp+1):
    cur_sum = 0

    for j in range(n):
        perf = get_performance(j, temp)
        cur_sum += perf

    max_sum = max(max_sum, cur_sum)

print(max_sum)