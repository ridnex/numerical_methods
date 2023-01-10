#Simpson’s rule

import sympy as sm
import math
x = sm.symbols('x')
f_x = x**3+1
a_limit = -2
b_limit = 2
num = 8
h = (b_limit-a_limit)/num

interval_points = []
for i in range(a_limit*10, b_limit*10+1, 5):
    interval_points.append(i/10)
print("Point in interval with h: ", interval_points)


solution = 0
for i in range(len(interval_points)):
    if i==0 or i==len(interval_points)-1:
        solution+=h/3*f_x.subs(x, interval_points[i])
    else:
        if i%2==1:
            solution+=h/3*f_x.subs(x, interval_points[i])*4
        else:
            solution+=h/3*f_x.subs(x, interval_points[i])*2
    
print("Solution by Simpson rule: ", solution)

direct_solution = sm.integrate(eval(str(f_x)), (x, a_limit, b_limit))
print("Direct solution by integration: ", direct_solution)

Error = abs(math.ceil(solution)- direct_solution)
print("error:   ", Error)

diff_f = sm.diff(f_x, x)
diff_ff = sm.diff(diff_f, x)
diff_fff = sm.diff(diff_ff, x)
diff_ffff = sm.diff(diff_fff, x)
theory_error = -1*(b_limit-a_limit)*diff_ffff.subs(x, b_limit)/180*h**4
print("Theory error: ", theory_error)
print("because 4 derivative _of_f(x)=0")