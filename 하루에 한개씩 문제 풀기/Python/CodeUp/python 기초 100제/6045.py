import sys

num_list = list(map(int,sys.stdin.readline().split()))

print(sum(num_list), round(sum(num_list)/len(num_list),2))