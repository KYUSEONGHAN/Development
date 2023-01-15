# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 2022 kakao blind recuritment, level2: 주차 요금 계산, python3
from math import ceil

def split_time(time: str):
    return map(int, time.split(':'))

def calculate_time(in_hour: int, in_minute: int, out_hour: int, out_minute: int) -> int:
    return (out_hour - in_hour) * 60 + (out_minute - in_minute)

def get_car_date_dict(records: list) -> dict:
    car_data_dict = {}

    for data in records:
        time, car_index, car_type = data.split()
        if car_index not in car_data_dict:
            car_data_dict[car_index] = {car_type: [time]}
        else:
            if car_type not in car_data_dict[car_index]:
                car_data_dict[car_index][car_type] = [time]
            else:
                car_data_dict[car_index][car_type].append(time)

    return car_data_dict

def get_car_index_time(car_data_dict: dict) -> dict:
    car_index_time = {}

    for key, value in car_data_dict.items():
        for index, time in enumerate((value['IN'])):
            in_hour, in_minute = split_time(value['IN'][index])
            try:
                out_hour, out_minute = split_time(value['OUT'][index])
            except:
                out_hour, out_minute = 23, 59
            if key not in car_index_time:
                car_index_time[key] = calculate_time(in_hour, in_minute, out_hour, out_minute)
            else:
                car_index_time[key] += calculate_time(in_hour, in_minute, out_hour, out_minute)

    return car_index_time

def get_parking_fees(fees: list, car_index_time: dict) -> list:
    answer = []

    for _, time in sorted(car_index_time.items(), key=lambda x: x[0]):
        money = fees[1] + ceil((time - fees[0]) / fees[2]) * fees[-1] if time > fees[0] else fees[1]
        answer.append(money)

    return answer

def solution(fees: list, records: list) -> list:
    car_data_dict = get_car_date_dict(records)

    car_index_time = get_car_index_time(car_data_dict)

    return get_parking_fees(fees, car_index_time)

if __name__ == '__main__':
    print(solution(
        fees=[180, 5000, 10, 600],  # 기본 시간, 기본 요금, 단위 시간, 단위 요금
        records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    ))  # [14600, 34400, 5000]
    print(solution(
        fees=[120, 0, 60, 591],
        records=["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
    ))  # [0, 591]
    print(solution(
        fees=[1, 461, 1, 10],
        records=["00:00 1234 IN"]
    ))  # [14841]