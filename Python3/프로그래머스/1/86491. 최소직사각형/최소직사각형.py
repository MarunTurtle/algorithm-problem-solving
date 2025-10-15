def solution(sizes):
    for size in sizes:
        size.sort()
    
    max_w = 0
    max_h = 0
    
    for size in sizes:
        max_w = max(max_w, size[0])
        max_h = max(max_h, size[1]) 
    
    return max_w * max_h