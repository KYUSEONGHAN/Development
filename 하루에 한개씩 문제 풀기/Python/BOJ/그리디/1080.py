# boj, 1080:행렬, python3
import sys
input = sys.stdin.readline

def othello(matrix, x, y):
    for i in range(3):
        for j in range(3):
            if matrix[x+i][y+j] == '0':
                matrix[x+i][y+j] = '1'
            else:
                matrix[x+i][y+j] = '0'

def solve(n, m, matrix_a, matrix_b):
    cnt = 0

    for x in range(n-2):
        for y in range(m-2):
            if matrix_a[x][y] != matrix_b[x][y]:
                othello(matrix_a, x, y)
                cnt += 1

    return -1 if matrix_a != matrix_b else cnt

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix_a = [list(map(str, input())) for _ in range(n)]
    matrix_b = [list(map(str, input())) for _ in range(n)]

    print(solve(n, m, matrix_a, matrix_b))