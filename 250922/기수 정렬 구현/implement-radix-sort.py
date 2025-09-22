n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def radix_sort(arr): 
    k = max(len(str(x)) for x in arr)

    for i in range(k):
        new_arr = [[] for _ in range(10)]

        for j in range(n):
            s = str(arr[j]).zfill(k)
            digit = int(s[-1-i])
            new_arr[digit].append(arr[j])

        store_arr = []
        for b in range(10):
            store_arr.extend(new_arr[b])
        arr = store_arr

    return arr

print(*radix_sort(arr))
