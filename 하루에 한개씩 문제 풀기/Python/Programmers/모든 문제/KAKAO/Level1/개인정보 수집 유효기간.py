# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# programmers, 20223 kakao blind, level1: 개인정보 수집 유효기간, python3
from dateutil.relativedelta import relativedelta
from datetime import datetime

def solution(today: str, terms: list, privacies: list) -> list:
    answer, dict = [], {}
    # type convert str to datetime
    today = datetime.strptime(today.replace('.', '-'), '%Y-%m-%d')

    for term in terms:
        alpa, month = term.split()
        if alpa not in dict:
            dict[alpa] = month

    for index, privacie in enumerate(privacies, start=1):
        time, alpa = privacie.split()
        time = datetime.strptime(time.replace('.', '-'), '%Y-%m-%d')
        if alpa not in dict:
            if today >= time:
                answer.append(index)
        else:
            if today >= time + relativedelta(months=int(dict[alpa])):
                answer.append(index)

    return answer

if __name__ == '__main__':
    print(solution(
        today="2022.05.19",
        terms=["A 6", "B 12", "C 3"],
        privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    ))  # [1, 3]
    print(solution(
        today="2020.01.01",
        terms=["Z 3", "D 5"],
        privacies=["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    ))  # [1, 4, 5]