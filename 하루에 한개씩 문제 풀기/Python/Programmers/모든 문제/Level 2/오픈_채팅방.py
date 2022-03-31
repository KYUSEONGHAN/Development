# https://programmers.co.kr/learn/courses/30/lessons/42888
# programmers, level2: 오픈 채팅방, python3
def solution(record: list) -> list:
    dict, answer = {}, []

    for x in record:
        data = list(map(str, x.split()))

        if data[0] == 'Enter':
            dict[data[1]] = data[2]
        elif data[0] == 'Change':
            dict[data[1]] = data[2]

    for x in record:
        data = list(map(str, x.split()))

        if data[0] == 'Enter':
            answer.append(dict[data[1]] + '님이 들어왔습니다.')
        elif data[0] == 'Leave':
            answer.append(dict[data[1]] + '님이 나갔습니다.')

    return answer

if __name__ == '__main__':
    recode = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]

    result = [
        "Prodo님이 들어왔습니다.",
        "Ryan님이 들어왔습니다.",
        "Prodo님이 나갔습니다.",
        "Prodo님이 들어왔습니다."
    ]

    print(solution(recode))