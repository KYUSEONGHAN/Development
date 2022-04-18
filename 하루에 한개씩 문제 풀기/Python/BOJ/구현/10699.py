# https://www.acmicpc.net/problem/10699
# boj, 10699: 오늘 날짜, python3
from datetime import datetime

def get_today_date() -> str:
    return datetime.today().strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(get_today_date())