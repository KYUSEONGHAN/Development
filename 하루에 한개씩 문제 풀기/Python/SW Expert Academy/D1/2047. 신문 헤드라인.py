# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QKsLaAy0DFAUq&categoryId=AV5QKsLaAy0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# sw expert academy, d1: 2047. 신문 헤드라인, python3
def solve(news_paper: str):
    return news_paper.upper()

if __name__ == '__main__':
    news_paper = str(input())
    print(solve(news_paper))