# 현재 위치
position = 0
visited = set([position])  # 최초 위치 0에서 시작
traveled = set()  # 두 번 이상 지나간 구간

N = int(input())  # 명령의 수

# 명령 처리
for _ in range(N):
    move, direction = input().split()
    move = int(move)  # 이동 거리
    
    if direction == "R":
        for i in range(position + 1, position + move + 1):
            if i in visited:
                traveled.add(i)  # 두 번 이상 지나간 구간 기록
            visited.add(i)
        position += move
    
    elif direction == "L":
        for i in range(position - 1, position - move - 1, -1):
            if i in visited:
                traveled.add(i)  # 두 번 이상 지나간 구간 기록
            visited.add(i)
        position -= move

# 두 번 이상 지나간 영역의 크기 출력
print(len(traveled)-1)
