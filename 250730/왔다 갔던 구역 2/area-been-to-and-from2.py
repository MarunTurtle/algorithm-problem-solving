n = int(input())  # 명령의 개수
history = {}  # 위치별 방문 횟수를 기록할 딕셔너리
position = 0  # 시작 위치는 0

# 명령 입력 받기
for _ in range(n):
    x, direction = input().split()
    x = int(x)
    
    for _ in range(x):
        if direction == 'L':
            position -= 1  # 왼쪽으로 이동
        else:
            position += 1  # 오른쪽으로 이동

        # 해당 위치를 기록
        if position in history:
            history[position] += 1
        else:
            history[position] = 1

# 두 번 이상 지나간 구간의 크기 계산
overlapped_area = 0
for count in history.values():
    if count >= 2:
        overlapped_area += 1

print(overlapped_area)
