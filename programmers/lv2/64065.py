# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s[2:-2].split('},{')
    list_of_sets = []
    for char in s:
        inner_list = []
        for x in char.split(','):
            inner_list.append(int(x))
        list_of_sets.append(inner_list)
    list_of_sets.sort(key=len)

    answer = []

    for current_list in list_of_sets:
        for num in current_list:
            if num not in answer:
                answer.append(num)
                break

    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
