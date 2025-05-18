def solution(numbers):
    sum = []
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            sum.append(numbers[i] + numbers[j])
            
    answer = sorted(set(sum))
    
    return answer