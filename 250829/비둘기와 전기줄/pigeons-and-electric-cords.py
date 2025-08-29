n = int(input())
birds = [tuple(map(int, input().split())) for _ in range(n)]
num_list = [2]*11
ans = 0

for bird in birds:
    # print(bird)
    idx, location = bird
    if num_list[idx] == 2:
        num_list[idx] = location
    elif num_list[idx] != location:
        ans += 1
        num_list[idx] = location
    else:
        continue

print(ans)