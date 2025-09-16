n, a, b = map(int, input().split())
result = [i for i in range(1, a)]
result.append(max(a, b))
result += [i for i in range(b-1, 0, -1)]
if len(result) > n:
    result = [-1]
else:
    result = result[0:1] + [1] * (n - len(result)) + result[1:]
import sys
sys.stdout.write(' '.join([str(r) for r in result]))