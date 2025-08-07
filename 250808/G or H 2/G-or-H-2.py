MAX_NUM = 100

# 변수 선언 및 입력
n = int(input())
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)
    
    arr[x] = 1 if c == 'G' else 2

# 모든 구간의 시작점을 잡아봅니다.
max_len = 0
for i in range(MAX_NUM + 1):
	for j in range(i + 1, MAX_NUM + 1):
		# i와 j 위치에 사람이 있는지 확인합니다.
		if arr[i] == 0 or arr[j] == 0:
			continue
		
		# 해당 구간 내 g와 h의 개수를 구합니다.
		cnt_g = 0
		cnt_h = 0
		
		for k in range(i, j + 1):
			if arr[k] == 1:
				cnt_g += 1
			if arr[k] == 2:
				cnt_h += 1
		
		# 조건을 만족할 때 구간의 길이를 구해 최댓값과 비교합니다.
		if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
			leng = j - i
			max_len = max(max_len, leng)

print(max_len)
