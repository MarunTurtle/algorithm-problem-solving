target_distance = 6368

def total_distance_with(n):
    return ((n * (n+1)) // 2) + (((n - 1) * (n)) // 2)

top_speed = 74
remaining_distance = 0
ans = float('inf')

while True:
    if total_distance_with(top_speed) > target_distance:
        break
    remaining_distance = target_distance - total_distance_with(top_speed)
    remainder = (remaining_distance // top_speed) + 1
    ans = min(ans, (top_speed * 2) - 1 + remainder)
    # print(f"top_speed {top_speed} total_distance {total_distance_with(top_speed)}, remaining_distance {remaining_distance} cur_ans {(top_speed * 2) - 1 + remainder}")
    top_speed += 1

print(ans)

