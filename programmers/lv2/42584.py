# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# def solution(prices):
#     answer = []

#     n = len(prices)
#     for i in range(n):
#         sec = 0
#         for j in range(i, n):
#             sec += 1
#             if prices[j] < prices[i]:
#                 break
#         answer.append(sec-1)
#     return answer

def solution(prices):

    stack = []
    result = [0] * len(prices)

    for i, price in enumerate(prices):
        # 스택이 비어있지 않고, 현재 가격이 이전 가격보다 작다면
        while stack and price < stack[-1][1]:
            prev_i, prev_price = stack.pop()
            result[prev_i] = i - prev_i
        stack.append((i, price))

    # 남은 것들은 끝까지 떨어지지 않은 것들
    while stack:
        prev_i, prev_price = stack.pop()
        result[prev_i] = len(prices) - 1 - prev_i
