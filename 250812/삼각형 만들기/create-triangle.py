n = int(input())
grids = [tuple(map(int, input().split())) for _ in range(n)]

def get_height(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        return abs(y1 - y2)        
    elif x2 == x3:
        return abs(y2 - y3)
    elif x3 == x1:
        return abs(y3 - y1)
    else:
        return 0
    
def get_base(x1, y1, x2, y2, x3, y3):
    if y1 == y2:
        return abs(x1 - x2)        
    elif y2 == y3:
        return abs(x2 - x3)
    elif y3 == y1:
        return abs(x3 - x1)
    else:
        return 0

def get_area(x1, y1, x2, y2, x3, y3):
    base = get_base(x1, y1, x2, y2, x3, y3)
    height = get_height(x1, y1, x2, y2, x3, y3)

    return base * height

max_area = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            area = get_area(grids[i][0], grids[i][1], grids[j][0], grids[j][1], grids[k][0], grids[k][1])
            max_area = max(max_area, area)

print(max_area)