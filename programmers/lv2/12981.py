# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    used = set([words[0]])

    for i in range(1, len(words)):
        curr_word = words[i]

        if curr_word[0] != words[i-1][-1] or curr_word in used:
            return [i % n + 1, i // n + 1]

        used.add(curr_word)

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
