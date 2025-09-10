x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

x3 = min(x1, a1)
y3 = min(y1, b1)

x4 = max(x2, a2)
y4 = max(y2, b2)

ans = abs(x3 - x4) * abs(y3 - y4)

print(ans)