n = int(input())
arr = list(map(int, input().split()))

def bubble_sort(arr):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                sorted = False
    return arr

print(*bubble_sort(arr))