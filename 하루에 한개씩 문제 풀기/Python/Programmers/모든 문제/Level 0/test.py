def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        print(N % 10, end="")
        N = N // 10


if __name__ == '__main__':
    print(solution(54321))
    print(solution(10011))
    print(solution(1))
    print(solution(7347))
    print(solution(98742))
    print(solution(4329042))

# 수정은 최대 3줄까지 허용
