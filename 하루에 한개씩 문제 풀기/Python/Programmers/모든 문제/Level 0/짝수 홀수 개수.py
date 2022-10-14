# https://school.programmers.co.kr/learn/courses/30/lessons/120824
# programmers, level 0: 짝수 홀수 개수, python3
def solution(num_list: list) -> list:
    answer = [0, 0]

    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))  # [2, 3]
    print(solution([1, 3, 5, 7]))     # [0, 4]