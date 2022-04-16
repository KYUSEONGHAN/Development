# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# sw expert acadmey, d1: 2068. 최대수 구하기, python3
def solve(nums: list) -> str:
    return str(max(nums))

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        nums = list(map(int, input().split()))
        print(f'#{i} {solve(nums)}')