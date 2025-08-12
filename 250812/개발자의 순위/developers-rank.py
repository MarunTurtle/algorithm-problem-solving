k, n = map(int, input().split())
games = [list(map(int, input().split())) for _ in range(k)]
count = 0

for i in range(1, n+1):      # 첫번째 숫자
    for j in range(1, n+1):  # 두번째 숫자
        is_stronger = True
        for game in games:
            if game.index(i) >= game.index(j):
                is_stronger = False

        if is_stronger:
            count += 1

print(count)