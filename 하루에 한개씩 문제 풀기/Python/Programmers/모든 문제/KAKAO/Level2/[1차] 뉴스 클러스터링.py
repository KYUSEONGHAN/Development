# https://school.programmers.co.kr/learn/courses/30/lessons/17677
# programmers, 2018 kakao, level2: [1차] 뉴스 클러스터링, python3
def zakad(str1: str, str2: str) -> int:
    set1, set2 = set(), set()
    # 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효
    for x in range(len(str1)):
        if str1[x:x+2].isalpha() and len(str1[x:x+2]) == 2:
            set1.add(str1[x:x+2])
    for x in range(len(str2)):
        if str2[x:x+2].isalpha() and len(str2[x:x+2]) == 2:
            set2.add(str2[x:x+2])

    intersection = set1 & set2
    union = set1 | set2

    if not intersection and not union:
        return 65536
    return int(65536 * (len(intersection) / len(union)))

def solution(str1: str, str2: str) -> int:
    # 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다.
    str1, str2 = str1.lower(), str2.lower()
    # 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다.
    score = zakad(str1, str2)
    return score
    # answer = 0
    # # 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다.
    # alpha_1 = ''.join(map(str, [x.lower() for x in str1 if x.isalpha()]))
    # alpha_2 = ''.join(map(str, [x.lower() for x in str2 if x.isalpha()]))
    #
    # set_1 = set(alpha_1[x:x+2] for x in range(len(alpha_1)) if len(alpha_1[x:x+2]) == 2)
    # set_2 = set(alpha_2[x:x+2] for x in range(len(alpha_2)) if len(alpha_2[x:x + 2]) == 2)
    #
    # intersection = set_1 & set_2
    # union = set_1 | set_2
    #
    # if not len(intersection):
    #     return int(65536 * (1 / len(union)))
    #
    # return int(65536 * (len(intersection) / len(union)))

if __name__ == '__main__':
    print(solution("FRANCE", "french"))    # 16384
    print(solution("handshake", "shake hands"))  # 65536
    print(solution("aa1+aa2", "AAAA12"))   # 43690
    print(solution("E=M*C^2", "e=m*c^2"))  # 65536