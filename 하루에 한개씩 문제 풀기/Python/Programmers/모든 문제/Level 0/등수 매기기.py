# https://school.programmers.co.kr/learn/courses/30/lessons/120882
# programmers, level0: 등수 매기기, python3
def solution(score: list) -> list:
    dict, avg_list = {}, [sum(num) / 2 for num in score]

    for index, avg in enumerate(sorted(avg_list, reverse=True), start=1):
        if avg not in dict:
            dict[avg] = index

    return [dict[avg] for avg in avg_list]

if __name__ == '__main__':
    print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))  # [1, 2, 4, 3]