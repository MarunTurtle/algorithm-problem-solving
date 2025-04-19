def to_seconds(time_str):
    mm, ss = map(int, time_str.split(':'))
    return mm * 60 + ss

def to_mmss(seconds):
    mm = seconds // 60
    ss = seconds % 60
    return f"{mm:02d}:{ss:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = to_seconds(video_len)
    cur = to_seconds(pos)
    op_start_sec = to_seconds(op_start)
    op_end_sec = to_seconds(op_end)

    for cmd in commands:
        # 1. 오프닝 스킵 먼저 적용
        if op_start_sec <= cur <= op_end_sec:
            cur = op_end_sec

        # 2. 명령어 처리
        if cmd == "prev":
            cur -= 10
            if cur < 0:
                cur = 0
        elif cmd == "next":
            cur += 10
            if cur > video_len_sec:
                cur = video_len_sec

    # 마지막에도 오프닝에 걸쳐 있는 경우 스킵
    if op_start_sec <= cur <= op_end_sec:
        cur = op_end_sec

    return to_mmss(cur)