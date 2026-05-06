# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    zeros = 0
    cnt = 0

    while s != '1':
        cnt += 1
        ones = s.count('1')
        zeros += len(s) - ones
        s = bin(ones)[2:]

    return [cnt, zeros]


print(solution("01110"))
