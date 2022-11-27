# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# programmers, level1: 숫자 짝꿍, python3
def solution(X: str, Y: str) -> str:
    answer = ""
    partner = set(X) & set(Y)

    if not partner:
        return '-1'

    for num in partner:
        answer += min(X.count(num), Y.count(num)) * num

    return ''.join(map(str, sorted(answer, reverse=True))) if sum([int(x) for x in answer]) != 0 else '0'

if __name__ == '__main__':
    print(solution("100", "2345"))     # "-1"
    print(solution("100", "203045"))   # "0"
    print(solution("100", "123450"))   # "10"
    print(solution("12321", "42531"))  # "321"
    print(solution("5525", "1255"))    # "552"
    print(solution("3403", "13203"))   # 330
    print(solution("5525", "1255"))    # 552