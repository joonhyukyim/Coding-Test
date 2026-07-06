# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)

    current_weight = 0
    time = 0

    while waiting or current_weight > 0:
        time += 1

        # 다리에서 트럭 한 대가 나감
        out_truck = bridge.popleft()
        current_weight -= out_truck

        # 새로운 트럭이 올라갈 수 있는지 확인
        if waiting and current_weight + waiting[0] <= weight:
            truck = waiting.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            # 이번 초에는 아무 트럭도 올라가지 않음
            bridge.append(0)

    return time
