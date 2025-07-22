n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def absolute(_list):
    for i in range(n):
        _list[i] = abs(_list[i])

absolute(arr)

print(*arr)
