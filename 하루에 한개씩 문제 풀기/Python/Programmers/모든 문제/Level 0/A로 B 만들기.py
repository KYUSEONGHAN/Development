# https://school.programmers.co.kr/learn/courses/30/lessons/120886
# programmers, level0: A로 B 만들기, Python3
def solution(before: str, after: str) -> int:
    before_dict, after_dict = {}, {}

    # before의 길이 == after의 길이여서
    for index in range(len(before)):
        if before[index] not in before_dict:
            before_dict[before[index]] = 1
        else:
            before_dict[before[index]] += 1
        if after[index] not in after_dict:
            after_dict[after[index]] = 1
        else:
            after_dict[after[index]] += 1

    return 1 if before_dict == after_dict else 0


if __name__ == '__main__':
    print(solution("olleh", "hello"))  # 1
    print(solution("allpe", "apple"))  # 0