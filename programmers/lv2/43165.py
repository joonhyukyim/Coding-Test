# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2

def solution(numbers, target):
    answer = 0

    def dfs(i, temp):
        nonlocal answer
        if i == len(numbers):
            if temp == target:
                answer += 1
        else:
            dfs(i+1, temp + numbers[i])
            dfs(i+1, temp - numbers[i])

    dfs(0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
