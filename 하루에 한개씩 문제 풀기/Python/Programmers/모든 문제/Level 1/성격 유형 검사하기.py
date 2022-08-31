# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# programmers, level1: 성격 유형 검사하기, python3
def solution(survey: list, choices: list) -> str:
    answer = ''
    indicators = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for index, data in enumerate(survey):
        if choices[index] == 1:
            indicators[data[0]] += 3
        elif choices[index] == 2:
            indicators[data[0]] += 2
        elif choices[index] == 3:
            indicators[data[0]] += 1
        elif choices[index] == 5:
            indicators[data[1]] += 1
        elif choices[index] == 6:
            indicators[data[1]] += 2
        elif choices[index] == 7:
            indicators[data[1]] += 3

    if indicators['R'] >= indicators['T']:
        answer += 'R'
    else:
        answer += 'T'

    if indicators['C'] >= indicators['F']:
        answer += 'C'
    else:
        answer += 'F'

    if indicators['J'] >= indicators['M']:
        answer += 'J'
    else:
        answer += 'M'

    if indicators['A'] >= indicators['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer

if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))  # "TCMA"
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))   # "RCJA"