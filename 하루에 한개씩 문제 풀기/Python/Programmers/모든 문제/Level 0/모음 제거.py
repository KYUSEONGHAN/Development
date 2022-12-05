# https://school.programmers.co.kr/learn/courses/30/lessons/120849
# programmers, level0: 모은 제거, python3
def solution(my_string: str) -> str:
    remove_list = ['a', 'e', 'i', 'o', 'u']

    for x in remove_list:
        my_string = my_string.replace(x, '')

    return my_string

if __name__ == '__main__':
    print(solution("bus"))  # "bs"
    print(solution("nice to meet you"))  # "nc t mt y"