# https://school.programmers.co.kr/learn/courses/30/lessons/120822
# programmers, level0: 문자열 뒤집기, python3
def solution(my_string: str) -> str:
    return my_string[::-1]  # 역슬라이싱

if __name__ == '__main__':
    print(solution("jaron"))  # "noraj"
    print(solution("bread"))  # "daerb"