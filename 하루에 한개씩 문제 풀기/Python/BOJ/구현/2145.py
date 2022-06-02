# https://www.acmicpc.net/problem/2145
# boj, 2145: 숫자 놀이, python3
def solve(num: str) -> str:  # 숫자놀이 계산 함수
    while True:              # 무한반복
        tmp = str(sum([int(x) for x in num]))  # 주어진 숫자의 각 자릿수를 더한다

        if len(tmp) == 1:    # 만일 계산한 값이 한 자릿수면
            break            # 무한반복 탈출
        else:                # 그렇지 않으면
            num = tmp        # 결과가 한 자릿수가 될 때 까지 규칙 1을 반복

    return tmp               # 계산된 값 반환

if __name__ == '__main__':  # main함수 시작
    while True:             # 무한반복문으로 숫자 입력 받음
        num = input()       # 입력받은 수의 각 자릿수를 계산해야하므로 string 설정

        if num == '0':      # 입력받은 수가 0이면 무한반복문 탈출
            break

        print(solve(num))   # 입력받은 수의 숫자놀이 값 출력