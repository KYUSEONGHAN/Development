# boj, 10828 : 스택, python3
import sys

n = int(sys.stdin.readline())

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else :
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack)==0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack)-1]

stack = []

for i in range(n):
    result = sys.stdin.readline().split()
    m = result[0]

    if m == 'push':
        push(result[1])
    elif m == 'pop':
        print(pop())
    elif m == 'size':
        print(size())
    elif m == 'top':
        print(top())
    elif m == 'empty':
        print(empty())
    else:
        print("input command error")
        break