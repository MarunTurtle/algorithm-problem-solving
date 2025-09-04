n = int(input())
seats = list(map(int, list(input())))
f_ans = 0 

def count_min_dist(seats):
    ans = 0
    diffs = []
    count = 0
    can_start = False 
    for i in range(n):
        if i == 0:
            if seats[i] == 1:
                can_start = True
            continue
        
        if seats[i] == 1:
            if can_start:
                count += 1 
                diffs.append(count)
                count = 0
            can_start = True
        if can_start:
            if seats[i] == 0:
                count += 1
    # print(diffs)
    return min(diffs)

for i in range(n):
    if seats[i] == 0:
        seats[i] = 1
        # print(f"r: {i} seats: {seats}")
        # print(count_min_dist(seats))
        f_ans = max(f_ans, count_min_dist(seats))
        seats[i] = 0

print(f_ans)
