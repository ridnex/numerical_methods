import matplotlib.pyplot as mp
import numpy as np

#
Error = 0.01
#functions:
f = lambda x: x**3+6*x-1

#interval:
def interval():
    for i in range(0, 2):
        for j in range(0,2):
            if f(i)*f(j)<0:
                return [i, j]

a, b = interval()
if a>b:
    a, b = b, a
    
print(a, b)
x0, x1 = a, b

print('{a:^10}{f_a:^20}|{c:^10}{f_c:^20}|{b:^10}{f_b:^20}|'.format(a='a', f_a="f(a)",c='c', f_c="f(c)",b='b', f_b="f(b)"))
print('-'*90)
c= float((a+b)/2)
arr = []
while abs(f(c))>Error:
    arr.append(c)
    print('{a1:^10}{f_a1:^20}|{c1:^10}{f_c1:^20}|{b1:^10}{f_b1:^20}|'.format(a1=a, f_a1=f(a),c1=c, f_c1=f(c),b1=b, f_b1=f(b)))
    
    if f(c)>0:
        b = c
    else:
        a = c
    c= float((a+b)/2)
arr.pop()

print(f"Answer: {c} ", f(c))


x = np.linspace(x0,x1)
mp.figure()
mp.plot(x, f(x), color = 'blue')
for i in arr:
    mp.scatter( i , f(i) , s = 50, c="red" )

mp.scatter( c , f(c), s = 100, c="yellow" ) 

mp.show()