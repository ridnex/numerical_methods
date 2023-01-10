import matplotlib.pyplot as mp
import numpy as np
from sympy import *
#
Error = 0.01
#functions:
x = symbols('x')
f_x = x**3+6*x-1
g_x = x**3+7*x-1
diff_f = diff(f_x, x)
diff_g = diff(g_x, x)
#interval:
x0, x1 = 0, 1

ex_diff_g_in_x0 =diff_g.subs(x, x0)
ex_diff_g_in_x1 =diff_g.subs(x, x1)
if(abs(ex_diff_g_in_x0)<1 and abs(ex_diff_g_in_x1)<1):
    print("Conferges")
else:
    print("Diverges, so evaluate another method")
    ex_diff_f_in_x0 = diff_f.subs(x, x0)
    ex_diff_f_in_x1 = diff_f.subs(x, x1)
    M = max(ex_diff_f_in_x0, ex_diff_f_in_x1)+1
    h_x = x - (f_x)/M
    p0 = x1
    i = 0
    cond = f_x.subs(x, p0)
    last_p= 0
    while cond>Error:
        i+=1
        last_p  = p0
        p0 = float(h_x.subs(x, p0))
        cond = float(f_x.subs(x, p0))
        print(f'x{i}= {p0},  f(x){i}={cond}')
    else:
        R_ERROR = abs(p0 - last_p)
        print("Error:", Error)
        print("R_Error:", R_ERROR)
        print(f'x={p0},   f(x)={cond}')



x = np.linspace(x0,x1)
g_x = x**3+7*x-1

mp.figure()
mp.plot(x, g_x, color = 'blue')
mp.plot(x, x, color = "red")
mp.plot(p0, cond, color = "black")
mp.scatter( p0 , cond , s = 100, c="black" ) 

mp.show()