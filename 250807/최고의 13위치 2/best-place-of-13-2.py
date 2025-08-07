import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = -sys.maxsize

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def count_coins(x, y):
    cnt = 0
    for i in range(3):
        if grid[x][y + i] == 1:
            cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if not in_range(i, j):
            continue

        temp_ans = count_coins(i, j)  # 첫 줄
        print(f"\n🔵 Start (i={i}, j={j}) → count_coins={temp_ans}")

        for k in range(i, n):
            if k == i:
                for l in range(j + 3, n):  # 같은 행에서는 겹치지 않게
                    if not in_range(k, l):
                        continue
                    temp_ans += count_coins(k, l)
                    print(f"  ➕ Add (k={k}, l={l}) → count_coins={count_coins(k, l)} → temp_ans={temp_ans}")
                    
                    ans = max(ans, temp_ans)
                    print(f"  🔺 max(ans, {temp_ans}) = {ans}")

                    temp_ans = count_coins(i, j)  # 초기화
                    print(f"  🔄 Reset temp_ans to {temp_ans}")
            else:
                for l in range(n):
                    if not in_range(k, l):
                        continue
                    temp_ans += count_coins(k, l)
                    print(f"  ➕ Add (k={k}, l={l}) → count_coins={count_coins(k, l)} → temp_ans={temp_ans}")
                    
                    ans = max(ans, temp_ans)
                    print(f"  🔺 max(ans, {temp_ans}) = {ans}")

                    temp_ans = count_coins(i, j)
                    print(f"  🔄 Reset temp_ans to {temp_ans}")

print("\n✅ Final Answer:", ans)