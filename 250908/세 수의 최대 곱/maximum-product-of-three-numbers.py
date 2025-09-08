from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
int_arr = [0] * 3  # 음수, 0, 양수
ans = float('-inf')

for i in range(n):
    if arr[i] > 0:
        int_arr[2] += 1
    elif arr[i] < 0:
        int_arr[0] += 1
    else:
        int_arr[1] += 1

if int_arr[0] == 0 and int_arr[2] == 0:
    ans = 0
elif int_arr[2] == 0 and int_arr[1] >= 1:
    ans = 0
elif int_arr[2] == 0 and int_arr[1] == 0:
    sort_arr = arr.sort(reverse=True)
    ans = sort_arr[0] * sort_arr[1] * sort_arr[2]
elif int_arr[0] == 0:
    sort_arr = arr.sort(reverse=True)
    ans = sort_arr[0] * sort_arr[1] * sort_arr[2]
else:
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                # if ans < arr[i] * arr[j] * arr[k]:
                #     print(arr[i], arr[j], arr[k])
                ans = max(ans, arr[i] * arr[j] * arr[k])
    
print(ans)