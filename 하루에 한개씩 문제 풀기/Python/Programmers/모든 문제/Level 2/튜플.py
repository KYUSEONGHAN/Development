# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# programmers, level2: 튜플, python3
def solution(s: str) -> list:
    answer, dict = [], {}
    remove_bracket = s.replace('{', '').replace('}', '').split(',')  # 괄호 제거 후, 쉼표를 구분하여 list화

    for x in remove_bracket:  # list화 한 input data를 dict에 추가
        if not x in dict:     # 만일, dict에 해당 데이터가 없으면
            dict[x] = 1       # 1 초기화
        else:                 # 선언이 되었던 데이터면
            dict[x] += 1      # +1 => 중복 입력 데이터를 처리하기 위함

    # value값이 높은 순에서 낮은순으로 내림차순 정렬
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    return [int(key) for key, _ in sorted_dict]  # 많이 선언된 순으로 list화하여 key값만 반환

if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
    print(solution("{{20,111},{111}}"))  # [111, 20]
    print(solution("{{123}}"))  # [123]
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))   # [3, 2, 4, 1]