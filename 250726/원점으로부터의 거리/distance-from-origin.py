n = int(input())

def get_distance(x, y):
    return abs(x) + abs(y)

# class Coord:
#     def __init__(self, x, y, idx):
#         self.x = x
#         self.y = y
#         self.idx = idx

coords = []
for i in range(1, n+1):
    x, y = tuple(map(int, input().split()))
    # idx = i
    # coord = Coord(x, y, idx)
    coords.append((get_distance(x, y), i))

coords.sort()

for _, idx in coords:
    print(idx)    