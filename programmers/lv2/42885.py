# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()

    boats = 0
    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        boats += 1

    return boats


print(solution([70, 50, 80, 50], 100))
