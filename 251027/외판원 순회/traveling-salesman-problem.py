import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
cost = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False] * n
picked = []

ans = INT_MAX


# 지금까지 방문한 지점의 수를 cnt라 했을 때
# 계속 탐색을 이어서 진행합니다.
def find_min(cnt):
    global ans

    # 모든 지점를 방문했을 때
    # 가능한 지금까지의 비용 합 중
    # 최솟값을 갱신합니다.
    if cnt == n:
        total_cost = 0
        for i in range(n - 1):
            curr_cost = cost[picked[i]][picked[i + 1]]
            # 만약 비용이 0이라면 불가능한 경우이므로 
            # 바로 함수를 빠져나옵니다.
            if curr_cost == 0:
                return
            
            total_cost += curr_cost

        # 최종적으로 1번 지점으로 다시 돌아오는 것 까지 고려해서 계산해줍니다.
        additional_cost = cost[picked[-1]][0]
        if additional_cost == 0:
            return

        # 답을 갱신해줍니다.
        ans = min(ans, total_cost + additional_cost)
        return

    # 방문할 지점을 선택합니다.
    for i in range(n):
        if visited[i]: 
            continue
        
        visited[i] = True
        picked.append(i)

        find_min(cnt + 1)

        visited[i] = False
        picked.pop()

   
# 1번 지점을 시작으로
# 탐색을 진행합니다.
visited[0] = True
picked.append(0)
find_min(1)

print(ans)
