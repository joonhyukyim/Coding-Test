from collections import deque


def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5

    cache = [''] * cacheSize

    cache = deque(cache)

    for city in cities:
        city = city.lower()
        if not city in cache:
            answer += 5
            cache.popleft()
        else:
            cache.remove(city)
            answer += 1
        cache.append(city)

    return answer
