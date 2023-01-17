# https://school.programmers.co.kr/learn/courses/30/lessons/72412
# programmers, 2021 kakao blind recuit, level2: 순위 검색, python3
from itertools import combinations
from bisect import bisect_left

def solution(info: list, query: list) -> list:
    answer, dict = [], {}

    for index, x in enumerate(info):
        key = x.split()[:-1]
        value = x.split()[-1]

        for y in range(5):
            for z in combinations(key, y):
                tmp = "".join(z)
                if tmp in dict:
                    dict[tmp].append(int(value))
                else:
                    dict[tmp] = [int(value)]

    for x in dict:
        dict[x].sort()

    for q in query:
        key = q.replace("and ", "").replace("-", "").split()[:-1]
        key = "".join(key)
        value = q.split()[-1]

        if key in dict:
            scores = dict[key]
            answer.append(len(scores) - bisect_left(scores, int(value)))
        else:
            answer.append(0)


    return answer

if __name__ == '__main__':
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))  # [1, 1, 1, 1, 2, 4]