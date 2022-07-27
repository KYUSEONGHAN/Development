# https://www.acmicpc.net/problem/4766
# boj, 4766: 일반 화학 실험, python3

def solve(temps: list):
    for x in range(len(temps)):
        if temps[x+1] == 999:
            break
        print('%.2f' % (temps[x+1] - temps[x]))

if __name__ == '__main__':
    temps = []

    while True:
        temp = float(input())
        temps.append(temp)

        if temp == 999:      # 입력 온도가 999면 무한반복문 탈출
            break

    solve(temps)