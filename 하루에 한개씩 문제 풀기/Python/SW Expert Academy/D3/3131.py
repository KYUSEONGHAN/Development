from typing import List

def eratos(n: int) -> List[int]:
    prime = [True] * (n+1)
    prime[0], prime[1] = False, False
    primes = []

    for x in range(2, n+1):
        if prime[x]:
            primes.append(x)
            for y in range(x*x, n+1, x):
                prime[y] = False

    return primes


if __name__ == '__main__':
    print(*eratos(100000))