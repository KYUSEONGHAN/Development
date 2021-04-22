# codeup, 1172 : 세 수 정렬하기, python3
import sys

def sort_num(num_list):
    return ' '.join(map(str,sorted(num_list)))

num_list = list(map(int, sys.stdin.readline().split(' ')))

print(sort_num(num_list))