# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n = len(maps)
    m = len(maps[0])

    queue = deque()
    queue.append((0, 0))

    check = [[False] * m for _ in range(n)]
    check[0][0] = True

    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            mx = cx + dx[i]
            my = cy + dy[i]

            if 0 <= mx < m and 0 <= my < n:
                if maps[my][mx] == 1 and not check[my][mx]:
                    check[my][mx] = True
                    dist[my][mx] = dist[cy][cx] + 1
                    queue.append((mx, my))

    if dist[n-1][m-1] == 0:
        return -1

    return dist[n-1][m-1]
