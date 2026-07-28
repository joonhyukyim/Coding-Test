# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):
    dt, df, ut, uf = fees
    parking = {}
    total_times = {}

    def time_to_minute(time_str):
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    for record in records:
        time_str, car, status = record.split()
        time = time_to_minute(time_str)

        if status == 'IN':
            parking[car] = time
        else:
            total_times[car] = total_times.get(
                car, 0) + (time - parking.pop(car))

    MAX_TIME = time_to_minute("23:59")
    for car, in_time in parking.items():
        total_times[car] = total_times.get(car, 0) + (MAX_TIME - in_time)

    answer = []
    for car, time in sorted(total_times.items()):
        if time <= dt:
            fee = df
        else:
            fee = df + (-(time - dt) // ut) * uf
        answer.append(fee)

    return answer
