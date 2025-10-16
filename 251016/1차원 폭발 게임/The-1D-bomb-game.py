n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# 폭발 시뮬레이션 함수
    # 연속이 없을 때까지
        # tmp배열 생성
        # 모든 숫자를 돌아가면서 보며
            # 연속일 경우에 idx 저장, 연속 v +=1
            # 연속이 끊겼을 때
                # M개 이상 연속 됐다면
                    # idx돌아가면서 0으로 초기화
                # 연속값 초기화
                # 현재값 초기화
            # 모든 숫자를 다 본다음에
                # 마지막으로 M개 이상 연속 됐는지 확인
        
        # 만약 tmp배열과 numbers 배열이 같다면:
            # 반복 끊기
        # 다르다면
            # tmp배열 -> numbers배열로 복사

def explode():
    global numbers

    hasExploded = True
    while hasExploded:
        # print(f"current numbers: {numbers}")
        hasExploded = False
        cat = 1
        idxs = [0]
        for i in range(1, len(numbers)):
            if numbers[i-1] != numbers[i]:
                if cat >= m:
                    # print(f"cat: {cat} idxs: {idxs} ")
                    for idx in idxs:
                        numbers[idx] = 0
                    hasExploded = True
                idxs = [i]
                cat = 1
            else:        
                cat += 1
                idxs.append(i)
            
            if i == len(numbers) - 1:
                if cat >= m:
                    # print(f"cat: {cat} idxs: {idxs} ")
                    for idx in idxs:
                        numbers[idx] = 0
                    hasExploded = True

        if hasExploded:
            tmp = []
            for i in range(len(numbers)):
                if numbers[i]:
                    tmp.append(numbers[i])     
            numbers = tmp
    
explode()

if numbers:
    print(len(numbers))
    for num in numbers:
        print(num)
else:
    print(0)