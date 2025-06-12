def solution(numbers):
    sums = set()
    
    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            sums.add(numbers[i] + numbers[i+j+1])
    
    return sorted(sums)