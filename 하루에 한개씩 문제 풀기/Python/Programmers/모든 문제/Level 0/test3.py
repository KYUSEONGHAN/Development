# kakao moblilty task 3, python
def solution(N: int, S: str) -> int:
    # 예약 좌석 목록은 공백으로 구분되어 주어진다.
    split_line = S.split()
    # 주어진 비행기 각 행, 렬의 예약 정보를 담을 dict 할당
    dict = {x: 0 for x in range(1, N+1)}
    # 비행기에 배치할 수 있는 최대 가족의 수를 담는 변수
    result = 0

    # for 반복문으로 순차적으로 공백으로 구분한 list를 순회
    for x in split_line:
        # A, K는 예약이 되있어도 4인가족의 예약에는 무관하므로 조건문으로 필터링
        if x[-1] != 'A' and x[-1] != 'K':
            # 만약 이번 비행기 라인에 예약되있는 정보가 지금까지 선언 안되었다면 바로 할당
            if dict[int(x[0])] == 0:
                dict[int(x[0])] = [x[-1]]
            # 만약 이번 비행기 라인에 예약되있는 정보가 여러개인 경우에는 list 자료구조에 추가
            else:
                dict[int(x[0])].append(x[-1])

    # 주어진 비행기 각 행, 렬의 예약 정보를 담은 dict 을 for 반복문으로 순차 순회
    for x in dict:
        # 해당 라인에 예약되있는 정보가 없다면
        if dict[x] == 0:
            # 최대 2 가구를 배치할 수 있다
            result += 2
        # 해당 라인에 예약 좌석이 1라면, 1가구를 배치할 수 있다.
        elif len(dict[x]) == 1:
            result += 1
        # 해당 라인에 여러개의 좌석이 예약되있는 경우
        else:
            # B, C, D, E 중 하나라도 예약이 되있는 상태에서 F, G, H, J 중 하나도 없으면 1개의 좌석 예약 가능
            if set(dict[x]) & {'B', 'C', 'D', 'E'} and not set(dict[x]) & {'F', 'G', 'H', 'J'}:
                result += 1
            # F, G, H, J 중 하나라도 예약이 되있는 상태에서 B C D E 중 하나도 없으면 1개의 좌석 예약 가능
            if set(dict[x]) & {'F', 'G', 'H', 'J'} and not set(dict[x]) & {'B', 'C', 'D', 'E'}:
                result += 1

    return result


if __name__ == '__main__':
    print(solution(N=2, S="1A 2F 1C"))  # 2
    print(solution(N=1, S=""))  # 2
    print(solution(N=22, S="1A 3C 2B 20G 5A"))  # 41

# A, K는 있어도 무상관하다
# 한 라인에 최대 2 가족을 배치할 수 있다.
# B가 예약되있는 상태에서 F, G, H, J 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0
# C가 예약되있는 상태에서 F, G, H, J 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0
# D가 예약되있는 상태에서 F, G, H, J 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0
# E가 예약되있는 상태에서 F, G, H, J 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0
# J가 예약되있는 상태에서 B, C, D, E 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0
# H가 예약되있는 상태에서 B, C, D, E 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0
# G가 예약되있는 상태에서 B, C, D, E 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0
# F가 예약되있는 상태에서 B, C, D, E 중 하나라도 예약이 되있으면 해당 라인은 배치 수 = 0