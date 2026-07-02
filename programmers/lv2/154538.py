# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque


def solution(x, y, n):
    visited = [False] * (y + 1)

    q = deque()
    q.append((x, 0))
    visited[x] = True

    while q:
        cur, cnt = q.popleft()

        if cur == y:
            return cnt

        for nxt in (cur + n, cur * 2, cur * 3):
            if nxt <= y and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt + 1))

    return -1


# def solution(x, y, n):
#     INF = float('inf')

#     dp = [INF] * (y + 1)
#     dp[x] = 0

#     for i in range(x, y + 1):
#         if dp[i] == INF:
#             continue

#         if i + n <= y:
#             dp[i + n] = min(dp[i + n], dp[i] + 1)

#         if i * 2 <= y:
#             dp[i * 2] = min(dp[i * 2], dp[i] + 1)

#         if i * 3 <= y:
#             dp[i * 3] = min(dp[i * 3], dp[i] + 1)

#     return dp[y] if dp[y] != INF else -1
