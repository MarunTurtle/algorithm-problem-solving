n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def get_max_num(x, arr):
    if x == n-1:
        return arr[x]
    return max(arr[x], get_max_num(x+1, arr))

print(get_max_num(0, arr))