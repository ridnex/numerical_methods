#Euler and Huens
import math
import sympy as sm
import matplotlib.pyplot as plt 
import numpy as np

x = sm.symbols('x')
y = sm.symbols('y')
d_y = 2*y-3*x
a_limit = 4
b_limit = 6
h = 0.5

y_exact = 6/4*x+3/4-27/4*math.e**(2*x-8) #by diff methods
y_arr = []
def dif_y(x, y):
    return 2*y -3*x

x_arr = list(np.arange(a_limit, b_limit+h, h))

for i in x_arr:
    y_arr.append(y_exact.subs(x, i))
print(y_arr)
def Euler():
    print('Euler:')
    y_arr = [0]
    y = 0
    cnt = 0
    for i in x_arr:
        y = y + h*(dif_y(i, y_arr[-1]))
        y_arr.append(y)
        print('X'+str(cnt)+':', i, "                 ", 'Y'+str(cnt+1)+':', y)
        cnt+=1
    return y_arr[:-1]


def Huens():
    print('Huens:')
    y_arr = [0]
    p_arr = []
    cnt = 1
    for i in x_arr:
        p = y_arr[-1] + h*(dif_y(i, y_arr[-1]))
        p_arr.append(p)
        y = y_arr[-1] + h/2*(dif_y(i, y_arr[-1])+dif_y(i+h, p))
        y_arr.append(y)
        print('X'+str(cnt-1)+':', i, "            ", 'P'+str(cnt)+':', p, "       ", 'Y'+str(cnt)+':', y)
        cnt+=1
    return y_arr[:-1]
Euler_y_arr = Euler()
Huens_y_arr = Huens()
error_E = abs(y_arr[-1]-Euler_y_arr[-1])
error_H = abs(y_arr[-1]-Huens_y_arr[-1])
print('Errors:  ')
print('Euler Error:         ', error_E, "         Const=", str(error_E/h))
print('Huens Error:         ', error_H, "         Const=", str(error_H/(h**2)))
plt.plot(x_arr, y_arr, color = "red", label = "Exact Graph")
plt.plot(x_arr, Euler_y_arr, color = "green", label = "The Euler graph")
plt.plot(x_arr, Huens_y_arr, color = "blue", label = "The Heun graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
