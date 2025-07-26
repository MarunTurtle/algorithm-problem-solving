n = int(input())

class Coord:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx

def get_distance(x, y):
    return abs(x - 0) + abs(y - 0)

coords = []
for i in range(1, n+1):
    x, y = tuple(map(int, input().split()))
    idx = i
    coord = Coord(x, y, idx)
    coords.append(coord)

coords.sort(key = lambda x: (get_distance(x.x, x.y), x.idx))

for coord in coords:
    print(f'{coord.idx}')
    