# https://school.programmers.co.kr/learn/courses/30/lessons/120835
# programmers, level0: 진료순서 정하기, python3
def solution(emergency: list) -> list:
    dict = {num: index for index, num in enumerate(sorted(emergency, reverse=True), start=1)}
    
    return [dict[x] for x in emergency]

if __name__ == '__main__':
    print(solution([3, 76, 24]))             # [3, 1, 2]
    print(solution([1, 2, 3, 4, 5, 6, 7]))   # [7, 6, 5, 4, 3, 2, 1]
    print(solution([30, 10, 23, 6, 100]))    # [2, 4, 3, 5, 1]