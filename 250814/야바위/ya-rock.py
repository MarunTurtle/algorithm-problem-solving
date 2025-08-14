n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

max_point = 0
max_location = 0

for i in range(1, 4):
    location_rock = i   # fixed location 1, 2, 3
    point = 0
    for j in range(n):
        # print(j, location_rock)
        if a[j] == location_rock:
            location_rock = b[j]
        elif b[j] == location_rock:
            location_rock = a[j]
        
        if location_rock == c[j]:
            point += 1

    if point > max_point:
        max_point = point
        max_location = i
    
print(max_point)
