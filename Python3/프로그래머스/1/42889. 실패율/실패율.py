def solution(N, stages):
    
    from collections import Counter
    
    # 스테이지 별로 dict에 저장
    stage_counts = Counter(stages)
    
    # 전체 플레이어 수 기록
    total_players = len(stages)
            
    # 실패율 저장 리스트 초기화 (스테이지 번호, 실패율 쌍 저장)
    failure = []

    # 1번부터 N번까지 반복하며 실패율 계산
    for stage in range(1, N+1):
        
        curr_stage = stage_counts[stage]
        
        # 분모가 0이면 실패율은 0으로 설정
        if curr_stage == 0:
            fail_rate = 0
        else:
            fail_rate = curr_stage / total_players

        # 실패율 리스트에 (스테이지, 실패율) 추가
        failure.append((stage, fail_rate))

        # 다음 스테이지 계산을 위해 현재 스테이지 인원을 전체 인원 수에서 제외
        total_players -= curr_stage

    # 실패율 기준 내림차순 정렬, 실패율 같으면 스테이지 번호 오름차순 정렬
    failure.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬된 스테이지 번호만 추출하여 리스트로 반환  
    return [stage for stage, _ in failure]
