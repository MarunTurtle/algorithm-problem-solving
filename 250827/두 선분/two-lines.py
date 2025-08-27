x1, x2, x3, x4 = map(int, input().split())

def is_intersecting(a, b, c, d):
    if b < c or d < a:
        return 'nonintersecting'
    else:
        return 'intersecting'

print(is_intersecting(x1, x2, x3, x4))