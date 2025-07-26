a, b, c = map(int, input().split())

# Please write your code here.
datetime1 = (11*24*60) + (11*60) + 11
datetime2 = (a*24*60) + (b*60) + c

print(datetime2 - datetime1) if datetime2 - datetime1 >= 0 else print(-1)