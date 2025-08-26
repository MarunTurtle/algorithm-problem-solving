from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 칸막이 후보 인덱스 (0 ~ n-2) 중에서 m-1개 선택
positions = range(1, n)  # 칸막이는 숫자 사이에 설치하므로 1부터 n-1까지

answer = float('inf')

# 모든 칸막이 조합에 대해 탐색
for cuts in combinations(positions, m - 1):
    cuts = list(cuts)
    cuts.append(n)  # 마지막 구간을 위해 끝 추가
    
    prev = 0
    max_sum = 0
    
    # 구간 합 계산
    for cut in cuts:
        segment_sum = sum(arr[prev:cut])
        max_sum = max(max_sum, segment_sum)
        prev = cut
    
    answer = min(answer, max_sum)

print(answer)