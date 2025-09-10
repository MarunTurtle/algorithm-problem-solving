n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

starts, ends = zip(*segments)
starts, ends = list(starts), list(ends)

starts.sort()
ends.sort()

first = ends[-2] - starts[0]
second = ends[-1] - starts[1]

print(min(first, second))