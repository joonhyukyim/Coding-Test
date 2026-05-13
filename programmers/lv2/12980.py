# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0

    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            ans += 1

    return ans


print(solution(5000))

# 비트연산자 풀이
# def solution(n):
#   return bin(n).count('1')
