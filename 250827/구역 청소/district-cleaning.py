a, b = map(int, input().split())
c, d = map(int, input().split())

def get_area(a, b, c, d):
    if b < c or d < a:
        return b - a + d - c
    else:
        return max(a, b, c, d) - min(a, b, c, d)

print(get_area(a, b, c, d))
