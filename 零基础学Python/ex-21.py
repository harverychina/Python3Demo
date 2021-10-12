# coding:utf-8
# 斐波纳契数列，指：一组数字，其中每个数字是前面两个数字的和。
fibo = [0, 1]
[fibo.append(fibo[-2] + fibo[-1]) for i in range(5)]
print(fibo)