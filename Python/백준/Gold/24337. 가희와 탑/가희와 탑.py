import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

result = [i for i in range(1, a)]
result.append(max(a, b))
result += [i for i in range(b-1, 0, -1)]

if len(result) > n:
    sys.stdout.write('-1')
    sys.exit(0)
else:
    result = result[0:1] + [1] * (n - len(result)) + result[1:]

sys.stdout.write(' '.join([str(r) for r in result]))