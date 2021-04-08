# boj, 1259 : 팰린드롬수, python3
def palindrome(n):
    n_reverse = list(reversed(n))

    return 'yes' if ''.join(n_reverse) == n else 'no'


while True:
    n = str(input())

    if n == '0':
        break

    print(palindrome(n))

# source == https://www.acmicpc.net/problem/1259