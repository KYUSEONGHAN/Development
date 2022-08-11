# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# programmers, level1: 체육복, python3
def solution(n: int, lost: list, reserve: list) -> int:
    answer, bunho = 0, [x for x in range(1, n+1)]  # bunho: 1번부터 n번까지 학생들 번호가 부여된 list
    overlap = list(set(lost).intersection(reserve))  # overlap: lost list와 reserve list 간의 중복 요소 추출

    if overlap:  # 만약 중복 요소가 있을 시,
        for x in overlap:   # 각 중복 요소마다
            lost.remove(x)  # lost list와 reserve list에 중복요소 삭제
            reserve.remove(x)

    num = min(len(lost), len(reserve))  # 아래에서 lost와 revese로 2중 반복문으로 순회할 것이므로 둘 중 작은 값을 체육복수로 지정

    for x in reserve:  # reserve 요소로 반복
        if num == 0:   # 빌려줄 수 있는 체육복 개수가 0이되면 반복문 탈출
            break
        for y in lost:  # lost 요소로 반복
            if y-1 == x or y+1 == x:  # 인접되는 번호라면
                answer += 1  # 빌려주기
                num -= 1  # 체육복 개수를 -1
                break     # 현재 번호에서 체육복을 빌려줬으니 break

    return n - len(lost) + answer  # (전체 학생 수) - (중복이 제거 된 잃어버린 체육복 수) + (빌려 줄 수 있는 체육복 수)

if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))  # 5
    print(solution(5, [2, 4], [3]))  # 4
    print(solution(3, [3], [1]))  # 2
    print(solution(8, [5, 6, 7], [4, 5]))  # 6
    print(solution(5, [4, 2], [3, 5]))  # 5
    print(solution(7, [2, 3, 4], [1, 2, 3, 6]))  # 6
    print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))  # 11
