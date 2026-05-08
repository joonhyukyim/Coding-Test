# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    ones = bin(n).count('1')
    next_num = n + 1
    while True:
        if bin(next_num).count('1') == ones:
            return next_num
        next_num += 1


print(solution(78))

# 비트 연산자 활용
# def solution(n):
#     c = n & -n
#     r = n + c
#     return (((r ^ n) >> 2) // c) | r
