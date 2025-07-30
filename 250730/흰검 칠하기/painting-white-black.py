# MAX_K 선언 100000
MAX_K = 100000
# n 입력
n = int(input())
# checked 배열 선언 -> 1: w 2: b
checked = [0] * (2 * MAX_K + 1)
# 흰색 배열 선언
check_w = [0] * (2 * MAX_K + 1)
# 검은색 배열 선언
check_b = [0] * (2 * MAX_K + 1)
# 검은색, 흰색, 회색 변수 선언
w, b, g = 0, 0, 0
# 현재 위치 cur 선언
cur = 0

# n까지 반복 하며 이동 입력 받기
for i in range(n):    
    # x, direction 입력 받기
    x, direction = tuple(input().split())
    x = int(x)
        # L일 때
    if direction == 'L':
        # x가 0 이상인 동안
        while x > 0:
            # 현재 위치 방문 표시
            checked[cur] = 1
            # 화이트 배열 방문 표시
            check_w[cur] += 1
            # x -= 1
            x -= 1
            # x가 0이 아니라면
            if x:
                # 현재 위치 왼쪽으로
                cur -= 1
    else:
    # R일 때
        # x가 0 이상인 동안
        while x > 0:        
            # 현재 위치 방문 표시
            checked[cur] = 2
            # 검정 배열 방문 표시
            check_b[cur] += 1
            # x -= 1
            x -= 1
            # x가 0이 아니라면
            if x:
                # 현재 위치 오른쪽으로
                cur += 1

# 전체 배열 확인
for i in range(2 * MAX_K + 1):
    # 만약 하얀색 배열 2 이상, 검은색 배열 2 이상이면
    if check_w[i] >= 2 and check_b[i] >= 2:
        # 회색 += 1
        g += 1
    # 전체 배열 확인 후 검은색
    elif checked[i] == 2:
        # 검은색 += 1
        b += 1
    # 전체 배열 확인 후 하얀색 
    elif checked[i] == 1:
        # 하얀색 += 1
        w += 1

# 출력
print(w, b, g)