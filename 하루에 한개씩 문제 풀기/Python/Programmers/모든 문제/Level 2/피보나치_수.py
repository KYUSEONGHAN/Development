# programmers, phase2:피보나치 수, python3
def solution(n):
    fibonacci = [0, 1]

    for i in range(2, n + 1):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

    return fibonacci[n] % 1234567