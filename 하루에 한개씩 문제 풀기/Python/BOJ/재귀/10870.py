# boj, 1259 : 피보나치수 5, python3
def fibonacci(num):
    if num <= 1:
	 return num
    return fibonacci(num-1) + fibonacci(num-2)
n = int(input())

print(fibonacci(n))

# source = https://www.acmicpc.net/problem/10870