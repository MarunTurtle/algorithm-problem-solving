def solution(N, stages):
    
    # 스테이지 별 도전자 수
    challenger = [0] * (N + 2)
    for stage in stages:
        challenger[stage] += 1
    
    # 스테이지별 실패한 사용자 수
    fails = {}
    total = len(stages)
    
    # 각 스테이지를 순회 하며, 실패율 계산
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
    
    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    
    return result


# def solution(N, stages):
#     from collections import Counter

#     total_players = len(stages)
#     counts = Counter(stages)
#     result = []

#     for stage in range(1, N + 1):
#         if total_players == 0:
#             fail_rate = 0
#         else:
#             fail = counts[stage]
#             fail_rate = fail / total_players
#             total_players -= fail
#         result.append((stage, fail_rate))

#     # 실패율 기준 내림차순 정렬, 실패율 같으면 번호 오름차순
#     result.sort(key=lambda x: (-x[1], x[0]))

#     return [stage for stage, _ in result]


# def solution(N, stages):
#     # 각 스테이지별 실패율을 저장할 리스트
#     fails = [0.0] * N

#     # 각 스테이지에 도달한 사용자 수를 저장할 리스트
#     num_users = [0] * N
    
#     # 각 스테이지 이상에 도달한 사용자 수 계산
#     for k in range(N):
#         for stage in stages:
#             if stage >= k + 1:
#                 num_users[k] += 1  
    
#     # 각 스테이지별 실패율 계산
#     for i in range(N):
#         if num_users[i] == 0:
#             # 스테이지에 도달한 사람이 없으면 실패율은 0
#             fails[i] = 0
#         else:
#             # 실패율 = 해당 스테이지에 머무른 사람 수 / 도달한 사람 수
#             fails[i] = stages.count(i + 1) / num_users[i]
    
#     # 실패율 기준으로 스테이지를 정렬해서 저장할 리스트
#     answer = []
    
#     # 각 스테이지(j)를 실패율이 높은 순으로 answer에 삽입
#     for j in range(N):
#         inserted = False
#         for idx in range(len(answer)):
#             # 현재 스테이지의 실패율이 더 높으면 해당 위치에 삽입
#             if fails[j] > fails[answer[idx]]:
#                 answer.insert(idx, j)
#                 inserted = True
#                 break
#             # 실패율이 같으면 스테이지 번호가 작은 쪽을 우선
#             elif fails[j] == fails[answer[idx]] and j < answer[idx]:
#                 answer.insert(idx, j)
#                 inserted = True
#                 break
#         # 삽입되지 않은 경우 맨 뒤에 추가
#         if not inserted:
#             answer.append(j)        
           
#     # 0-based 인덱스를 1-based 스테이지 번호로 변환
#     return [x + 1 for x in answer]
