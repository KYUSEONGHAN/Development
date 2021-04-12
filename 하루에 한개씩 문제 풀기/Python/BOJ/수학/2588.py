# (런타임 에러)
# boj, 2588 : 곱셈, python3
import sys

num1 = str(sys.stdin.readline())
num2 = str(sys.stdin.readline())

num1_list = list(map(int, num1))
num2_list = list(map(int, num2))

print(int(num1)*num2_list[-1])
print(int(num1)*num2_list[-2])
print(int(num1)*num2_list[0])
print(int(num1)*int(num2))


# (성공)
import sys

num1 = int(sys.stdin.readline())
num2= int(sys.stdin.readline())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)