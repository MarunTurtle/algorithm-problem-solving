n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
total = 0

for query in queries:
    for i in range(query[0]-1 , query[1]):
        total += arr[i]
    print(total)
    total = 0