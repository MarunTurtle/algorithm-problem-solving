from itertools import combinations

n = int(input())
sort_arr = list(map(int, input().split()))
sort_arr.sort(reverse=True)
int_arr = [0] * 3  # 음수, 0, 양수
ans = float('-inf')

for i in range(n):
    if sort_arr[i] > 0:
        int_arr[2] += 1
    elif sort_arr[i] < 0:
        int_arr[0] += 1
    else:
        int_arr[1] += 1

if int_arr[0] == 0 and int_arr[2] == 0:
    ans = 0
elif int_arr[2] == 0 and int_arr[1] >= 1:
    ans = 0
elif int_arr[2] == 0 and int_arr[1] == 0:
    ans = sort_arr[0] * sort_arr[1] * sort_arr[2]
elif int_arr[0] == 0:
    ans = sort_arr[0] * sort_arr[1] * sort_arr[2]
elif int_arr[2] == 1:
    ans = arr[0] * arr[n-1] * arr[n-2]
elif int_arr[0] == 1:
    ans = arr[0] * arr[1] * arr[2]
else: 
    ans_sub_1 = sort_arr[0] * sort_arr[1] * sort_arr[2]
    ans_sub_2 = sort_arr[n-1] * sort_arr[n-2] * sort_arr[0]
    ans = max(ans_sub_2, ans_sub_1)
    
print(ans)