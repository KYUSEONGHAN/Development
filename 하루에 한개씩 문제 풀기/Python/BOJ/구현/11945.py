# https://www.acmicpc.net/problem/11945
# boj, 11945: 뜨거운 붕어빵, python3

# 입력으로 주어진 list를 좌우로 뒤집히게하는 함수
def solve(l: list) -> str:
   return '\n'.join([x[0][::-1] for x in l])

if __name__ == '__main__':
    n, m = map(int, input().split())
    if m == 0:
        print()
    else:
        bungabbang = [list(map(str, input().split())) for _ in range(n)]
        print(bungabbang)
        print(solve(bungabbang))