# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a % 1234567


print(solution(100000))
