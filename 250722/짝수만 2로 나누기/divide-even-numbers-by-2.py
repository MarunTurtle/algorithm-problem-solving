n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def divide_by_two(_list):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2

divide_by_two(arr)

print(*arr)