# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def is_valid(string):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()
    return len(stack) == 0


def solution(s):
    answer = 0
    n = len(s)

    for x in range(n):
        rotated_s = s[x:] + s[:x]
        if is_valid(rotated_s):
            answer += 1

    return answer


print(solution("[](){}"))
