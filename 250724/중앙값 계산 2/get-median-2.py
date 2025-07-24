n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
def get_median(x):
    return x//2 + 1

new_arr = [0]

for i in range(1, n+1):
    new_arr.append(arr[i])
    new_arr.sort()
    if i % 2 == 1:
        print(new_arr[get_median(i)], end=" ")