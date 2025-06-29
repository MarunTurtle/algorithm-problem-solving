def solution(str1, str2):
    
    l = len(str1)
    ans = ''
    
    for i in range(l):
        ans += str1[i]+str2[i]
   
    return ans