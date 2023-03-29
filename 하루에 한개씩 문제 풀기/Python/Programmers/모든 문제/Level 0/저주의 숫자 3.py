# https://school.programmers.co.kr/learn/courses/30/lessons/120871/
# programmers, level0: 저주의 숫자 3, python3
def solution(n: int) -> int:
    answer = 0

    for x in range(n):
        answer += 1
        while (answer % 3 == 0 or '3' in str(answer)):
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution(15))  # 25
    print(solution(40))  # 76