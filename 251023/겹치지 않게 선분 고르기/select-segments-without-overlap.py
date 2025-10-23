# 변수 선언 및 입력:

n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0
selected_segs = list()


def overlapped(seg1, seg2):
    (ax1, ax2), (bx1, bx2) = seg1, seg2

    # 두 선분이 겹치는지 여부는
    # 한 점이 다른 선분에 포함되는 경우로 판단 가능합니다. 
    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
           (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)


def possible():
    # 단 한쌍이라도 선분끼리 겹치면 안됩니다
    for i, seg1 in enumerate(selected_segs):
        for j, seg2 in enumerate(selected_segs):
            if i < j and overlapped(seg1, seg2):
                return False

    return True


def find_max_segments(cnt):
    global ans
    
    if cnt == n:
        if possible():
            ans = max(ans, len(selected_segs))
        return
    
    selected_segs.append(segments[cnt])
    find_max_segments(cnt + 1)
    selected_segs.pop()
    
    find_max_segments(cnt + 1)


find_max_segments(0)
print(ans)
