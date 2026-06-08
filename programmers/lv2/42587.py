# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([(v, i) for i, v in enumerate(priorities)])

    while queue:
        curr_p, curr_i = queue.popleft()

        if any(curr_p < item[0] for item in queue):
            queue.append((curr_p, curr_i))
        else:
            answer += 1
            if curr_i == location:
                return answer
