# # https://school.programmers.co.kr/learn/courses/30/lessons/150370
# # kakao, 2023 카카오 블라인드 채용, level1: 개인정보 수집 유효기간, python3
# from dateutil.relativedelta import relativedelta
#
# def solution(today: str, terms: list, privacies: list) -> list:
#     for x in privacies:
#         print(today - relativedelta)
#
# if __name__ == '__main__':
#     print(solution(
#         today="2022.05.19",
#         terms=["A 6", "B 12", "C 3"],
#         privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
#     ))  # [1, 3]
#     print(solution(
#         today="2020.01.01",
#         terms=["Z 3", "D 5"],
#         privacies=["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
#     ))  # [1, 4, 5]
#
#
#     # privacies+ temrs >= today
from dateutil.relativedelta import relativedelta
from datetime import datetime

today = "2022.05.19"
year = int(today[:4])
month = int(today[5:7])
day = int(today[8:])

today = datetime(year, month, day)

print(today)

privacies = "2019.01.01"
year = int(privacies[:4])
month = int(privacies[5:7])
day = int(privacies[8:])

privacies = datetime(year, month, day)

print(privacies - relativedelta(month=9))