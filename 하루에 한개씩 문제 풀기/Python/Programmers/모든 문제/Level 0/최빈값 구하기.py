# https://school.programmers.co.kr/learn/courses/30/lessons/120812
# programmers, level0: 최빈값 구하기, python3
def solution(array: list) -> int:
    dict = {}

    # for 반복문으로 입력 list 순회
    for num in array:
        # 딕셔너리에 현재 값이 할당되있지 않다면 1 할당
        if num not in dict:
            dict[num] = 1
        # 그렇지 않을 시, 증감
        else:
            dict[num] += 1

    # 딕셔너리의 벨류값 기준으로 desc 정렬
    result = sorted(dict.items(), key=lambda x: x[-1], reverse=True)

    if len(result) <= 1:
        return result[0][0]
    # 최빈값이 여러개면, -1 반환
    return result[0][0] if result[0][-1] != result[1][-1] else -1

if __name__ == '__main__':
    print(solution([1, 2, 3, 3, 3, 4]))  # 3
    print(solution([1, 1, 2, 2]))  # -1
    print(solution([1]))  # 1