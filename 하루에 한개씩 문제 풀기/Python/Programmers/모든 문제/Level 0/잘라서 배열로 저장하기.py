# https://school.programmers.co.kr/learn/courses/30/lessons/120913
# programmers, level0: 잘라서 배열로 저장하기, python3
def solution(my_str: str, n: int) -> list:
    return [my_str[x:x+n] for x in range(0, len(my_str), n)]

if __name__ == '__main__':
    print(solution("abc1Addfggg4556b", 6))
    print(solution("abcdef123", 3))
