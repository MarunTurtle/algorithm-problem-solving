a, b, x, y = map(int, input().split())

direct = abs(b - a)
teleport1 = abs(x - a) + abs(y - b)
teleport2 = abs(y - a) + abs(x - b)

ans = min(direct, teleport1, teleport2)

print(ans)