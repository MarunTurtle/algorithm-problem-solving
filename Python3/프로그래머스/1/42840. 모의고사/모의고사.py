def solution(answers):
    
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    result = []
    
    max_score = 0
    
    for i, pattern in enumerate(patterns):
        score = 0
        for j, answer in enumerate(answers):
            place = j % len(pattern)
            if answer == pattern[place]:
                score += 1
        if score > max_score:
            result = [i+1]
            max_score = score
        elif score == max_score:
            result.append(i+1)
                                
    return result