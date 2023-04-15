# https://www.acmicpc.net/problem/8911
# boj, 8911: 거북이, Python3
def solve(test_case: str) -> int:
    x, y = 0, 0    # 거북이는 가장 처음에 (0, 0)에 있고 (각 x, y의 위치를 담은 변수)
    dx, dy = 0, 1  # 북쪽을 쳐다보고 있다.  (각 x, y의 방향을 담은 변수)
    max_x, min_x, max_y, min_y = 0, 0, 0, 0  # 각 거북이가 이동한 영역의 x, y 최대, 최소 값을 저장하는 변수

    for case in test_case:  # 입력받은 test_case를 for 반복문으로 순차 조회
        if case == 'F':  # F: 한 눈금 앞으로
            x += dx
            y += dy
        elif case == 'B':  # B: 한 눈금 뒤로
            x -= dx
            y -= dy
        elif case == 'L':  # L: 왼쪽으로 90도 회전
            dx, dy = - dy, dx
        elif case == 'R':  # R: 오른쪽으로 90도 회전
            dx, dy = dy, -dx

        # 거북이가 이동한 영역을 포함하는 가장 작은 직사각형을 이동할때마다 계산
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형의 넓이 반환
    return (max_x - min_x) * (max_y - min_y)

if __name__ == '__main__':
    t = int(input())  # 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

    for _ in range(t):
        test_case = str(input())  # 컨트롤 프로그램이 주어진다.

        print(solve(test_case))