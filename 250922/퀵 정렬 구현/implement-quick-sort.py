n = int(input())
arr = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # 중간 값 기준으로 피벗 선택
    left = [x for x in arr if x < pivot]   # 피벗보다 작은 값들
    equal = [x for x in arr if x == pivot] # 피벗과 같은 값들
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 값들
    
    return quick_sort(left) + equal + quick_sort(right)

print(*quick_sort(arr))
