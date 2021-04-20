import sys

visit_list = list(map(int,sys.stdin.readline().split()))
cnt = 1

while True:
    if cnt%visit_list[0]==0 and cnt%visit_list[1]==0 and cnt%visit_list[2]==0:
        print(cnt)
        break
    cnt += 1