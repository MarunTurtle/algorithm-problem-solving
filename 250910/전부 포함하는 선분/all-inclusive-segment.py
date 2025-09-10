n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

segments.sort(key = lambda x:x[0])
option1 = list(segments)
# print(option1)
del option1[0]
# print(option1)

s, e = zip(*option1)
s, e = list(s), list(e)
s.sort()
e.sort()
# print(s)
# print(e)

ans1 = abs(min(s) - max(e))
# print(ans1)

# print("-----")
segments.sort(key = lambda x:x[1])
option2 = list(segments)
# print(option2)
del option2[-1]
# print(option2)

s, e = zip(*option2)
s, e = list(s), list(e)
s.sort()
e.sort()
# print(s)
# print(e)

ans2 = abs(min(s) - max(e))
# print(ans2)

print(min(ans1, ans2))