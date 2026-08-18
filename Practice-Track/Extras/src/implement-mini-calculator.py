def mini_calculator(num1,num2,op):
    if op == "+":
        return num1 + num2
    elif op ==  "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1/num2

num1 = int(input())
num2 = int(input())
op = input()

print(mini_calculator(num1,num2,op))