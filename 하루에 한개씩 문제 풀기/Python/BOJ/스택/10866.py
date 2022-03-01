# https://www.acmicpc.net/problem/10866
# boj, 10866: 덱, python3
from collections import deque


def push_front_x(queue, num):
    queue.appendleft(num)

def push_back_x(queue, num):
    queue.append(num)

def pop_front(queue):
    if not len(queue):
        return -1

    num = queue.popleft()

    return num

def pop_back(queue):
    if not len(queue):
        return -1

    num = queue.pop()

    return num

def size(queue):
    return len(queue)

def empty(queue):
    return 0 if queue else 1

def front(queue):
    return queue[0] if queue else -1

def back(queue):
    return queue[-1] if queue else -1

def solve(order_list):
    # 큐 선언
    queue = deque()

    for order in order_list:
        if order == 'pop_front':
            print(pop_front(queue))
        elif order == 'pop_back':
            print(pop_back(queue))
        elif order == 'size':
            print(size(queue))
        elif order == 'empty':
            print(empty(queue))
        elif order == 'front':
            print(front(queue))
        elif order == 'back':
            print(back(queue))
        else:
            order, num = order.split()
            if order == 'push_front':
                push_front_x(queue, num)
            else:
                push_back_x(queue, num)


if __name__ == '__main__':
    n = int(input())
    order_list = [str(input()) for _ in range(n)]

    solve(order_list)
