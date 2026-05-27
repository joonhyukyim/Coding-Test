# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import Counter


def solution(want, number, discount):
    answer = 0

    want_dict = {want[i]: number[i] for i in range(len(want))}

    for i in range(len(discount) - 9):
        current_10_days = discount[i:i+10]
        discount_dict = Counter(current_10_days)
        if want_dict == discount_dict:
            answer += 1

    return answer
