# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        temp = 0
        while (temp < n):
            temp += i
            i += 1
        if temp == n:
            answer += 1
    return answer


print(solution(15))
