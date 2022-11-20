# https://school.programmers.co.kr/learn/courses/30/lessons/120839
# programmers, level0: 가위 바위 보, python3
def solution(rsp: str) -> str:
    dict = {"2": "0", "0": "5", "5": "2"}

    return "".join(map(str, [dict[x] for x in rsp]))

if __name__ == '__main__':
    print(solution("2"))    # "0"
    print(solution("205"))  # "052"