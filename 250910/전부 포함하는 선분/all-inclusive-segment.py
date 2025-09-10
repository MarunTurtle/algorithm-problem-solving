n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

starts, ends = zip(*segments)
starts, ends = list(starts), list(ends)

starts.sort()
ends.sort()

print(starts)
print(ends)

first = ends[-2] - starts[0]
second = ends[-1] - starts[1]

print(first, second)
print(min(first, second))