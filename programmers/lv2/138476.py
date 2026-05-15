# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter


def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_counts = sorted(count.values(), reverse=True)

    answer = 0
    total_picked = 0

    for c in sorted_counts:
        total_picked += c
        answer += 1
        if total_picked >= k:
            break

    return answer
