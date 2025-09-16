import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

if a + b - 1 > n:
    sys.stdout.write('-1')
    sys.exit(0)

result = [i for i in range(1, a)]
result.append(max(a, b))
result += [i for i in range(b-1, 0, -1)]
result = result[0:1] + [1] * (n - len(result)) + result[1:]

sys.stdout.write(' '.join([str(r) for r in result]))