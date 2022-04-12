# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
# sw expert academy, d2: 1989. 초심자의 회문 검사, python3
def solve(word: str) -> int:
    return 1 if word == word[::-1] else 0

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        word = str(input())
        print('#' + str(i) + ' ' + str(solve(word)))