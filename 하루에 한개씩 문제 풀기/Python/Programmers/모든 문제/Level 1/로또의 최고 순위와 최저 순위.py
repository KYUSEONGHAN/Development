# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# programmers, level1: 로또의 최고 순위와 최저 순위, python3
def solution(lottos: list, win_nums: list) -> list:
    # 맞힌 개수에 따른 순위 dictionary
    hits = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    hit_num, zero_num = 0, 0  # hit_num: 로또 맞힌 개수, zero_num: 0 개수

    for lotto in lottos:
        if lotto in win_nums:
            hit_num += 1
        if lotto == 0:
            zero_num += 1

    return [hits[hit_num + zero_num], hits[hit_num]]

if __name__ == '__main__':
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))   # [1, 6]
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))   # [1, 1]