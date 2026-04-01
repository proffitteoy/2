# 1. 输入一个包含若干数字的列表，输出其中绝对值最大的数字
lst = eval(input())
print(max(lst, key=abs))

# 2. 输入一个包含任意整数的列表，输出这些数字的乘积
lst = eval(input())
product = 1
for x in lst:
    product *= x
print(product)