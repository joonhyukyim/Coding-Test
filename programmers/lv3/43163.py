# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 최소는 bfs가 효율적이다.

from collections import deque


def solution(begin, target, words):

    if target not in words:
        return 0

    word_length = len(begin)

    q = deque([(begin, 0)])
    visited = set([begin])

    while q:
        current_word = q.popleft()
        if current_word[0] == target:
            return current_word[1]
        for word in words:
            if word not in visited:
                diff = 0
                for i in range(word_length):
                    if word[i] != current_word[0][i]:
                        diff += 1
                if diff == 1:
                    visited.add(word)
                    q.append((word, current_word[1] + 1))


# def solution(begin, target, words):
#     if target not in words:
#         return 0

#     answer  = 0

#     array_length = len(words)
#     word_length = len(begin)

#     counts = []
#     visited = [False] * array_length

#     def dfs(string, cnt):
#         if visited and string == target:
#             counts.append(cnt)
#             return
#         for i in range(array_length):
#             if not visited[i]:
#                 diff = 0
#                 for j in range(word_length):
#                     if string[j] != words[i][j]:
#                         diff += 1
#                 if diff == 1:
#                     visited[i] = True
#                     dfs(words[i], cnt + 1)
#                     visited[i] = False
#     dfs(begin, 0)

#     if counts:
#         answer = min(counts)

#     return answer
