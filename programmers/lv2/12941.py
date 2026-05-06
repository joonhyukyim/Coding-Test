# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))


print(solution([1, 4, 2], [5, 4, 4]))
