n = int(input())
arr = list(map(int, input().split()))

expected = n
for x in reversed(arr):
    if x == expected:
        expected -= 1

print(expected)
