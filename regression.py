import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f = open('temp.csv', 'r')
rdr = csv.reader(f)

arr = []
arr2 = []

for line in rdr:
    if line == 0:
        print("pass")
    else:
        arr.append(line[3])
        arr2.append(line[4])

aa = np.array(arr)
bb = np.array(arr2)
print(aa)

temp = np.array([22.4,
                 22.1,
                 22.2,
                 22.1,
                 21.8,
                 21.9,
                 22.4,
                 23.2,
                 24.2,
                 25.9,
                 27.2,
                 28.2,
                 29.2,
                 30.2,
                 31.2,
                 31.3,
                 31.4,
                 30.5,
                 29.1,
                 27.7,
                 26,
                 25.1,
                 24.6,
                 24.3,
                 23.7,
                 23.3,
                 22.7,
                 22.1,
                 21.7,
                 21.7,
                 22.2,
                 23.5,
                 25.1,
                 26,
                 26.5,
                 26.8,
                 27.3,
                 27.4,
                 27.1,
                 27.4,
                 27,
                 26.8,
                 26.3,
                 25.6,
                 24.6,
                 24.1,
                 23.5,
                 23,
                 22.5,
                 22.4,
                 21.7,
                 21.4,
                 21,
                 20.7,
                 21.5,
                 23.7,
                 25.6,
                 27.5,
                 29.1,
                 30.7,
                 31.9,
                 32.7,
                 33.1,
                 33,
                 32,
                 30.7,
                 29.7,
                 28.1,
                 27.2,
                 26.5,
                 26,
                 25.6,
                 25.1,
                 23.8,
                 22.6,
                 22.1,
                 22.2,
                 22.1,
                 22.4,
                 22.7,
                 23.2,
                 23.4,
                 24.3,
                 26.4,
                 27.9,
                 28.2,
                 28.5,
                 28.6,
                 28.5,
                 26.9,
                 24.9,
                 23,
                 22.2,
                 21.4,
                 20.8,
                 20.1,
                 19.7,
                 19.3,
                 19.1,
                 18.8,
                 18.3,
                 18.2,
                 19.1,
                 20.2,
                 21.9,
                 23.6,
                 25.5,
                 26.5,
                 27,
                 27.7,
                 28.6,
                 27.3,
                 26.8,
                 26,
                 24.4,
                 23.5,
                 22.6,
                 21.4,
                 21,
                 21.1,
                 20.8,
                 20.5,
                 20.1,
                 20.1,
                 20,
                 20.1,
                 20.4,
                 21.1,
                 22.4,
                 23.4,
                 25.4,
                 27.2,
                 28.5,
                 29.5,
                 30.4,
                 30.4,
                 29.6,
                 28,
                 26.8,
                 25.9,
                 24.9,
                 23.9,
                 22.8,
                 22.2,
                 ])
print("arr mean:", np.mean(temp))
xMean = np.mean(aa)
print("xMean:", xMean)

yMean = np.mean(bb)

# 독립변수와 종속변수의 편차를 구한다.


xx = aa - xMean

xxsum = sum(xx)

print(xxsum)

yy = bb - yMean

yysum = sum(yy)

print(yysum)

# 독립변수와 종속변수의 편차제곱의 합을 구한다.

powXX = pow(xx, 2)

print(powXX)

powXXsum = sum(powXX)

print(powXXsum)

powYY = pow(yy, 2)

powYYsum = sum(powYY)

print(powYYsum)

# 독립변수와 종속변수의 편차를 곱한다.

xxyy = xx * yy

xxyysum = sum(xxyy)

print(xxyysum)

# a = x와 y 편차 곱의 합 / xx편자 곱의 합

a = xxyysum / powXXsum

print(" a %f " % (a))

# b = 종속변수 평균 - 독립변수 평균 * a

b = yMean - xMean * a

print("b %f " % (b))

# 회귀식  y = ax -b의 값을 구한 것

# 회귀식의 그래프에 독립변수 평균, 종속변수 평균이 만나는 점이 반드시 지나간다.

print(" y = 3.7x - 36.4")
