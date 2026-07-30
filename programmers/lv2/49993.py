# https://school.programmers.co.kr/learn/courses/30/lessons/49993

from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skill_queue = deque(skill)
        is_valid = True

        for s in tree:
            if s in skill:
                if s != skill_queue.popleft():
                    is_valid = False
                    break

        if is_valid:
            answer += 1

    return answer
