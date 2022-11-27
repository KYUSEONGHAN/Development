# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# programmers, level1: 신고 결과 받기, python3
def solution(id_list: list, report: list, k: int) -> list:
    report_dict = {x: 0 for x in id_list}
    kakao_dict = {x: 0 for x in id_list}
    kakao_report = []
    answer = []

    for x in report:
        reportor, reported = x.split()
        if not report_dict[reportor]:
            report_dict[reportor] = {reported: 1}
        else:
            if reported not in report_dict[reportor]:
                report_dict[reportor][reported] = 1

    for index, x in enumerate(report_dict):
        if report_dict[x] == 0:
            pass
        else:
            for y in report_dict[x]:
                kakao_dict[y] += 1

    for x in kakao_dict:
        if kakao_dict[x] >= k:
            kakao_report.append(x)

    for x in report_dict:
        cnt = 0
        if type(report_dict[x]) == dict:
            for y in report_dict[x]:
                if y in kakao_report:
                    cnt += 1
            answer.append(cnt)
        else:
            answer.append(0)

    return answer





if __name__ == '__main__':
    print(solution(
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
            2
        )
    )  # [2,1,1,0]
    print(solution(
            ["con", "ryan"],
            ["ryan con", "ryan con", "ryan con", "ryan con"],
            3
        )
    )  # [0, 0]