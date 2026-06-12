# https: // school.programmers.co.kr/learn/courses/30/lessons/17677

# from collections import Counter


# def solution(str1, str2):
#     def make_multiset(s):
#         s = s.lower()
#         result = []

#         for i in range(len(s) - 1):
#             pair = s[i:i+2]

#             if pair.isalpha():
#                 result.append(pair)

#         return Counter(result)

#     A = make_multiset(str1)
#     B = make_multiset(str2)

#     intersection = sum((A & B).values())
#     union = sum((A | B).values())

#     if union == 0:
#         return 65536

#     return int(intersection / union * 65536)


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    multiset1 = []
    multiset2 = []

    for i in range(len(str1)-1):
        if str1[i] in alphabet and str1[i+1] in alphabet:
            multiset1.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if str2[i] in alphabet and str2[i+1] in alphabet:
            multiset2.append(str2[i:i+2])

    # Jaccard Similarity
    if not multiset1 and not multiset2:
        return 65536
    else:
        m1_len = len(multiset1)
        m2_len = len(multiset2)
        intersection = 0
        multiset2_copy = multiset2.copy()
        for char in multiset1:
            if char in multiset2_copy:
                intersection += 1
                multiset2_copy.remove(char)
        union = m1_len + m2_len - intersection
        return intersection / union * 65536 // 1
