




grid = [[x * 3  for x in map(int, input().split())] for _ in range(3)]

for row in grid:
    for num in row:
        print(num, end=" ")
    print()