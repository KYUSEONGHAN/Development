# boj, 10845: 큐, python3
from collections import deque

def push(queue, x):
    queue.appendleft(x)

def pop(queue):
    if not queue:
        print(-1)
    else:
        print(queue[-1])
        queue.pop()

def size(queue):
    print(len(queue))

def empty(queue):
    if not queue:
        print(1)
    else:
        print(0)

def front(queue):
    if queue:
        print(queue[-1])
    else:
        print(-1)

def back(queue):
    if queue:
        print(queue[0])
    else:
        print(-1)

def solve(order_list):
    queue = deque()

    for x in order_list:
        if x == 'pop':
            pop(queue)
        elif x == 'size':
            size(queue)
        elif x == 'empty':
            empty(queue)
        elif x == 'front':
            front(queue)
        elif x == 'back':
            back(queue)
        else:
            push_num = x.split()[-1]
            push(queue, push_num)

if __name__ == '__main__':
    n = int(input())
    order_list = [str(input()) for _ in range(n)]

    solve(order_list)