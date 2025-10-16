n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

def explode():
    global numbers
    while True:
        # ✅ 비었으면 바로 종료 (빈 리스트에서 idx 0 접근 방지)
        if not numbers:
            break

        hasExploded = False
        cat = 1
        idxs = [0]

        for i in range(1, len(numbers)):
            if numbers[i-1] != numbers[i]:
                if cat >= m:
                    for idx in idxs:
                        numbers[idx] = 0
                    hasExploded = True
                idxs = [i]
                cat = 1
            else:
                cat += 1
                idxs.append(i)

        # 마지막 구간 마감
        if cat >= m:
            for idx in idxs:
                numbers[idx] = 0
            hasExploded = True

        if hasExploded:
            # 0을 제거해 압축
            numbers = [x for x in numbers if x != 0]
        else:
            break

explode()

if numbers:
    print(len(numbers))
    for num in numbers:
        print(num)
else:
    print(0)
