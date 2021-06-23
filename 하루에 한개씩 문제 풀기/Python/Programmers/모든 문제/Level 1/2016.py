# programmers, phase1 : 2016, python3
from datetime import date

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

def solution(a, b):
    return days[date(2016, a, b).weekday()]