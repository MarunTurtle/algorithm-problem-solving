OFFSET = 1000
MAX_R = 2000

# 변수 선언 및 입력
n = int(input())
segments = []

# 현재 위치
cur = 0

for _ in range(n):
	distance, direction = tuple(input().split())
	distance = int(distance)
	
	if direction == 'L':
		# 왼쪽으로 이동할 경우 : cur - distance ~ cur까지 경로 이동
		section_left = cur - distance
		section_right = cur
		cur -= distance
	else:
		# 오른쪽으로 이동할 경우 : cur ~ cur + distance까지 경로 이동
		section_left = cur
		section_right = cur + distance
		cur += distance
	
	segments.append([section_left, section_right])

	
checked = [0] * (MAX_R + 1)

for x1, x2 in segments:
	# OFFSET을 더해줍니다.
	x1, x2 = x1 + OFFSET, x2 + OFFSET
	
	# 구간을 칠해줍니다.
	# 구간 단위로 진행하는 문제이므로
	# x2에 등호가 들어가지 않음에 유의합니다.
	for i in range(x1, x2):
		checked[i] += 1

# 2번 이상 지나간 영역의 크기를 구합니다.
cnt = 0
for elem in checked:
	if elem >= 2:
		cnt += 1
print(cnt)
