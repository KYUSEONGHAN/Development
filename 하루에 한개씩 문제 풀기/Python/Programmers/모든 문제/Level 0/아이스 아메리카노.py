# https://school.programmers.co.kr/learn/courses/30/lessons/120819
# programmes, level0: 아이스 아메리카노, python3
def solution(money: int) -> list:
    return [money // 5500, money % 5500]

if __name__ == '__main__':
    print(solution(5500))    # [1, 0]
    print(solution(15000))   # [2, 4000]