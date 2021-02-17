# kakao_2021_blind #5
# #누적합(Prefix Sum) (#투포인터)
# 최대 99:59:59 = 360000초 이므로 1초당 한칸씩 배열잡아서 구간에 몇명이 보는지 확인해야함
# 단순하게 완탐으로 생각하면 O(N*M) 이상이 되는데, 이러면 시간초과남
# 누적합 이용하면 O(N)으로 가능
# 투포인터도 사용 가능


def solution(play_time, adv_time, logs):
    play_time = string_to_sec(play_time)  # maximum 99:59:59 = 360000sec
    adv_time = string_to_sec(adv_time)

    total_time = [0 for _ in range(play_time + 1)]
    target_times = [0]  # 00:00:00도 포함해야함
    for log in logs:
        start, end = log.split('-')
        start = string_to_sec(start)
        end = string_to_sec(end)
        total_time[start] += 1
        total_time[end] -= 1
        target_times.append(start)
        target_times.append(end - adv_time)  # 음수일수도 있음

    for i in range(play_time + 1):
        if i == 0:
            continue
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(play_time + 1):
        if i == 0:
            continue
        total_time[i] = total_time[i] + total_time[i - 1]

    time_at_max = 1000000
    max_viewtime = 0
    for i in range(play_time - adv_time + 1):
        if i == 0:
            viewtime = total_time[i + adv_time - 1]
        else:
            viewtime = total_time[i + adv_time - 1] - total_time[i - 1]
        if max_viewtime < viewtime:
            max_viewtime = viewtime
            time_at_max = i

    answer = sec_to_string(time_at_max)

    return answer


def string_to_sec(string):
    time = 0
    h, m, s = map(lambda s: int(s), string.split(':'))
    total_sec = h * 3600 + m * 60 + s
    return total_sec


def sec_to_string(seconds):
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return f'{hour:0>2}:{minute:0>2}:{second:0>2}'


play_time_ = "50:00:00"
adv_time_ = "50:00:00"
logs_ = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time_, adv_time_, logs_))
