# boj, 1924: 2007년, python3
import sys
import calendar

input = sys.stdin.readline

def solve(month, day):
    week = {0: 'MON', 1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN'}

    return week[calendar.weekday(2007, month, day)]

if __name__ == '__main__':
    x, y = map(int, input().split())

    print(solve(x, y))