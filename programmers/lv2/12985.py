# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    answer = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer

# return ((a - 1) ^ (b - 1)).bit_length()
