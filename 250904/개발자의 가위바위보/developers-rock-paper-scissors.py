import itertools

n = int(input())
matches = [tuple(map(int, input().split())) for _ in range(n)]
me, you = zip(*matches)
me, you = list(me), list(you)
max_ans = 0

scenarios = list(itertools.permutations([1, 2, 3], 3))

for scenario in scenarios:
    # print(f"scenario: {scenario}")
    ans = 0
    for i in range(n):
        a = me[i]
        b = you[i]
        power_a = scenario.index(a)
        power_b = scenario.index(b)
        # print(power_a, power_b)

        if power_a == 2 and power_b == 0:
            continue
        elif power_a == 0 and power_b == 2:
            ans += 1
        elif power_a > power_b:
            ans += 1
    max_ans = max(max_ans, ans)

print(max_ans)