def solution(answers):

    # 수포자 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 수포자 별 정답 갯수
    scores = [0] * 3
    
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
        
#     # 수포자 별 정답 맞춰보기
#     for i in range(3):
        
#         # 수포자 패턴의 길이
#         p_len = len(patterns[i])
        
#         # 정답 수 파악
#         ans = 0
        
#         # 문제 배열 내 모든 정답 확인
#         for j in range(num_problems):
#             # n번째 문제의 비교 정답 위치 계산
#             k = (j % p_len)

#             # 만약 j번째 문제와 i번째 학생의 k번째 정답과 일치한다면
#             if answers[j] == patterns[i][k]:
#                 # 정답 수 하나 증가
#                 ans += 1
#         # 최종 정답 수 저장
#         num_answers[i] = ans
        
    # 최고 점 찾기
    max_score = max(scores)
    
    answer = [i + 1 for i in range(3) if scores[i] == max_score]
        
    return answer