# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(current_k, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        for i in range(len(dungeons)):
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                dfs(current_k - dungeons[i][1], cnt+1)
                visited[i] = False

    dfs(k, 0)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
