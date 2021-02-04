def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n  # 60 분

    while start < end:
        mid = (start + end) // 2  # 30
        people = sum([mid // x for x in times])
        if people < n:
            start = mid + 1 # 중요
        elif people >= n:
            answer = mid
            end = mid - 1

    return answer