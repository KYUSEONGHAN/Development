# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
# sw expert academy, d2: 2005. 파스칼의 삼각형, python3
from typing import List  # type hint 명시용.

# 하위 구간에서 정해진 값이 나오는 패턴을 발견 -> 다이나믹 프로그래밍 알고리즘으로 접근
def solve(testcase: int) -> List[List[int]]:
    # dp table 초기화
    # 파스칼 입력 데이터를 행렬 2차원 list로 할당
    dp = [[0 for _ in range(x+1)] for x in range(testcase)]
    dp[0][0] = 1

    # DP bottom-up
    for i in range(1, testcase):
        for j in range(i+1):
            if j == 0:   # paskal 맨 왼쪽 데이터일 경우, 바로 위 맨 왼쪽 데이터 값과 동일
                dp[i][j] = dp[i-1][j]
            elif i == j:  # paskal 맨 오른쪽 데이터일 경우, 바로 위 맨 오른쪽 데이터 값과 동일
                dp[i][j] = dp[i-1][j-1]
            else:  # 맨 왼쪽 ~ 맨 오른쪽 데이터일 경우, 위에서 왼쪽과 오른쪽 숫자의 합으로 구성
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp

if __name__ == '__main__':
    t = int(input())  # 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,

    for index in range(1, t+1): # 그 아래로 각 테스트 케이스가 주어진다.
        print(f'#{index}')

        testcase = int(input())

        for x in solve(testcase):
            print(*x)