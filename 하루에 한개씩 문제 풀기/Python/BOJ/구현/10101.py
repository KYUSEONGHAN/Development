# https://www.acmicpc.net/problem/10101
# boj, 10101: 삼각형 외우기, python3
def solve(sizes: list) -> str:
    if sizes[0] == 60 and sizes[1] == 60 and sizes[-1] == 60:
        return 'Equilateral'

    if sum(sizes) == 180:
        if (sizes[0] == sizes[1] or sizes[0] == sizes[-1] or sizes[1] == sizes[-1]):
            return 'Isosceles'
        if sizes[0] != sizes[1] and sizes[0] != sizes[-1] and sizes[1] != sizes[-1]:
            return 'Scalene'

    return 'Error'

if __name__ == '__main__':
    # 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.
    sizes= [int(input()) for _ in range(3)]

    # 문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.
    print(solve(sizes))