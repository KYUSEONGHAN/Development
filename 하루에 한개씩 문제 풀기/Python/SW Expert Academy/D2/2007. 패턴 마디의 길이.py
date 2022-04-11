# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
# sw expert academy, d2: 2007. 패턴 마디의 길이, python3
def solve(word: str) -> int:
    for x in range(1, len(word)):
        if word[:x] == word[x:x*2]:
            return x

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        word = str(input())
        print('#' + str(i) + ' ' + str(solve(word)))