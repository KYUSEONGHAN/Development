# boj, 5585 : 거스름돈, python3
import sys

input_money = int(sys.stdin.readline())
money_list = [500,100,50,10,5,1]

if input_money >= 1000 or input_money < 1:
    print("range error")
else:
    money = 1000 - input_money
    result = 0
    for i in money_list:
        result += money//i
        money %= i
    print(result)