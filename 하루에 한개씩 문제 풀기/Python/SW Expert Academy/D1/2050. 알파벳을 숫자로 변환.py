# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# sw expert academy, d1: 2050. 알파벳을 숫자로 변환, python3
def solve(alpa: str) -> list:
    alpa_dict = {chr(y): x+1 for x, y in enumerate(range(ord('A'), ord('Z')+1))}

    return [alpa_dict[x] for x in alpa]

if __name__ == '__main__':
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    alpa = str(input())
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
    print(*solve(alpa))