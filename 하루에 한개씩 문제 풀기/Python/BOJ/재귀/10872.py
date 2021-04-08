# boj, 10872 : 팩토리얼, python3
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

n=int(input())
print(factorial(n))
