n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.
max_idx = n + 1
max_val = 0

while max_idx != 1:
    max_val = 0
    for i in range(1, max_idx):
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
    print(max_idx, end=" ")

