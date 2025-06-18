from collections import Counter

def solution(N, stages):
    
    stage_counts = Counter(stages)
    total_players = len(stages)
    failure = []

    for stage in range(1, N+1):
        
        curr_stage = stage_counts[stage]
        
        if curr_stage == 0:
            fail_rate = 0
        else:
            fail_rate = curr_stage / total_players

        failure.append((stage, fail_rate))

        total_players -= curr_stage

    failure.sort(key=lambda x: (-x[1], x[0]))
    
    return [stage for stage, _ in failure]
