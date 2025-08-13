n = int(input())
icebergs = [int(input()) for _ in range(n)]

# Please write your code here.
max_count = 0

for w in range(max(icebergs)+1):
    prev_status = 0
    count = 0
    for iceberg in icebergs:
        if iceberg - w <= 0:
            cur_status = 0  # it is sunk
        else:
            cur_status = 1
    
        if cur_status != prev_status:
            if cur_status == 1 and prev_status == 0:
                count += 1
            prev_status = cur_status
    
    max_count = max(max_count, count)

print(max_count)