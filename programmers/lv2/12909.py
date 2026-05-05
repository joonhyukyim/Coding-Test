# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    depth = 0

    for char in s:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1

        if depth < 0:
            return False

    return depth == 0


print(solution("(()"))
